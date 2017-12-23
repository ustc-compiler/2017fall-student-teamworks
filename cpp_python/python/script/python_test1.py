from traits.api import Delegate, HasTraits, Instance, Int, Str

class Parent ( HasTraits ):
    last_name = Str( 'Zhang' )

class Child ( HasTraits ):
    age = Int
    father = Instance( Parent )

    last_name = Delegate( 'father' )
    def _age_changed ( self, old, new ):
        print 'Age changed from %s to %s ' % ( old, new )



p = Parent()
c = Child()

c.father = p

c.configure_traits()