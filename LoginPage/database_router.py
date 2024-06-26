class LocationRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'myapp':
            return 'default'
        return 'location_backup'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'myapp':
            return 'default'
        return 'location_backup'

    def allow_relation(self, obj1, obj2, **hints):
        if (obj1._meta.app_label == 'myapp' and
                obj2._meta.app_label == 'myapp'):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == 'default':
            # Se o banco de dados padrão estiver fora do ar, 
            # use o banco de dados de backup
            return False
        elif db == 'location_backup':
            # Permita a migração apenas para o banco de dados de backup
            return app_label != 'myapp'
        return None
