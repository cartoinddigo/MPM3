class ActionRouter(object): 
    def db_for_read(self, model, **hints):
        "Point all operations on action models to 'actiondb'"
        if model._meta.app_label == 'action':
            return 'baseaction'
        return 'default'

    def db_for_write(self, model, **hints):
        "Point all operations on action models to 'actiondb'"
        if model._meta.app_label == 'action':
            return 'baseaction'
        return 'default'
    
    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a both models in action app"
        if obj1._meta.app_label == 'action' and obj2._meta.app_label == 'action':
            return True
        # Allow if neither is action app
        elif 'action' not in [obj1._meta.app_label, obj2._meta.app_label]: 
            return True
        return False
    
    def allow_syncdb(self, db, model):
        if db == 'baseaction' or model._meta.app_label == "action":
            return False # we're not using syncdb on our legacy database
        else: # but all other models/databases are fine
            return True