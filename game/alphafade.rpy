init python:
    class AlphaInterpolate(renpy.display.core.Displayable):
        """
        This displayable has two children. It interpolates between the positions
        of its two children to place them on the screen.
        """
        
        def __init__(self, delay, old, new, use_old, time_warp):
            super(AlphaInterpolate, self).__init__()
            
            
            self.old = old
            self.new = new
            
            
            self.use_old = use_old
            
            
            self.time_warp = time_warp
            
            
            self.delay = delay
            self.st = 0
        
        def render(self, width, height, st, at):
            old_r = renpy.display.render.render(self.old, width, height, st, at)
            new_r = renpy.display.render.render(self.new, width, height, st, at)
            
            if self.use_old:
                cr = old_r
            else:
                cr = new_r
            
            self.st = st
            
            if self.st < self.delay:
                renpy.display.render.redraw(self, 0)
            
            if self.st > self.delay:
                done = 1.0
            else:
                done = self.st / self.delay
            
            if self.time_warp is not None:
                done = self.time_warp(done)
            
            absolute = renpy.display.core.absolute
            
            def I(a, b):
                return absolute(a + done * (b - a))
            
            old_alpha = old_r.alpha
            new_alpha = new_r.alpha
            
            cr.alpha = I(old_alpha, new_alpha)
            
            return cr
        def get_placement(self):
            if self.use_old:
                return self.old.get_placement()
            else:
                return self.new.get_placement()

    def AlphaFadeTransition(delay, old_widget=None, new_widget=None, enter=None, leave=None, old=False, layers=[ 'master', 'upper', 'overui' ], time_warp=None, enter_time_warp=None, leave_time_warp=None):
        use_old = old
        
        def merge_slide(old, new):
            
            
            
            
            
            if (not isinstance(new, renpy.display.layout.MultiBox)
                or (new.layers is None and new.layer_name is None)):
                
                if old is new:
                    return new
                else:
                    return AlphaInterpolate(delay, old, new, use_old, time_warp)
            
            
            
            
            if new.layers:
                
                rv = renpy.display.layout.MultiBox(layout='fixed')
                
                for layer in renpy.config.layers:
                    
                    f = new.layers[layer]
                    
                    if (isinstance(f, renpy.display.layout.MultiBox)
                        and layer in layers
                        and f.scene_list is not None):
                        
                        f = merge_slide(old.layers[layer], new.layers[layer])
                    
                    rv.add(f)
                
                return rv
            
            
            
            
            
            
            def wrap(sle):
                return renpy.display.layout.AdjustTimes(sle.displayable, sle.show_time, sle.animation_time)
            
            def tag(sle):
                return sle.tag or sle.displayable
            
            def merge(sle, d):
                rv = sle.copy()
                rv.show_time = 0
                rv.displayable = d
                return rv
            
            def entering(sle):
                
                if not enter:
                    return
                
                new_d = wrap(new_sle)
                move = AlphaInterpolate(delay, enter(new_d), new_d, False, enter_time_warp)
                rv_sl.append(merge(new_sle, move))
            
            def leaving(sle):
                
                if not leave:
                    return
                
                old_d = wrap(sle)
                move = AlphaInterpolate(delay, old_d, leave(old_d), True, leave_time_warp)
                move = renpy.display.layout.IgnoresEvents(move)
                rv_sl.append(merge(old_sle, move))
            
            
            def moving(old_sle, new_sle):
                
                if old_sle.displayable is new_sle.displayable:
                    rv_sl.append(new_sle)
                    return
                
                old_d = wrap(old_sle)
                new_d = wrap(new_sle)
                
                move = AlphaInterpolate(delay, old_d, new_d, use_old, time_warp)
                
                rv_sl.append(merge(new_sle, move))
            
            
            
            old_sl = old.scene_list[:]
            new_sl = new.scene_list[:]
            rv_sl = [ ]
            
            
            old_map = dict((tag(i), i) for i in old_sl if i is not None)
            new_tags = set(tag(i) for i in new_sl if i is not None)
            rv_tags = set()
            
            while old_sl or new_sl:
                
                
                if old_sl:
                    
                    old_sle = old_sl[0]
                    old_tag = tag(old_sle)
                    
                    
                    if old_tag in rv_tags:
                        old_sl.pop(0)
                        continue
                    
                    
                    
                    if old_tag not in new_tags:
                        leaving(old_sle)
                        rv_tags.add(old_tag)
                        old_sl.pop(0)
                        continue
                
                
                
                
                
                new_sle = new_sl.pop(0)
                new_tag = tag(new_sle)
                
                
                if new_tag in old_map:
                    old_sle = old_map[new_tag]
                    
                    moving(old_sle, new_sle)
                    rv_tags.add(new_tag)
                    continue
                
                else:
                    entering(new_sle)
                    rv_tags.add(new_tag)
                    continue
            
            
            
            rv_sl.sort(key=lambda a : a.zorder)
            
            layer = new.layer_name
            rv = renpy.display.layout.MultiBox(layout='fixed', focus=layer, **renpy.game.interface.layer_properties[layer])
            rv.append_scene_list(rv_sl)
            
            return rv
        
        
        rv = merge_slide(old_widget, new_widget)
        rv.delay = delay
        
        return rv
    AlphaFade = renpy.curry(AlphaFadeTransition)