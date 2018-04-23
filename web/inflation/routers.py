from .models import CoreModel

class CoreRouter(object):
    
    def db_for_read(self, model, **hints):
        print('DEBUG - db_for_read - model: ' + repr(model) + ' **hints: ' + str(hints))
        if issubclass(model, CoreModel):
            return 'core'
        return 'default'
    
    def db_for_write(self, model, **hints):
        print('DEBUG - db_for_write - model: ' + repr(model) + ' **hints: ' + str(hints))
        if issubclass(model, CoreModel):
            return None
        return 'default'
    
    def allow_relation(self, obj1, obj2, **hints):
        print('DEBUG - allow_relation - obj1: ' + repr(obj1) + ' obj2: ' + repr(obj2) + ' **hints: ' + str(hints))
        if obj1._state.db == obj2._state.db:
            return True
        return None
    
    #def allow_migrate(self, db, app_label, model_name=None, **hints):
        #print('DEBUG - allow_migrate - db: ' + repr(db) + ' app_label: ' + repr(app_label) + ' model_name: ' + model_name + ' **hints: ' + str(hints))
        #if db == 'core':
        #    return False
        #return None

