from django.db.models import Manager, QuerySet

__author__ = 'agerasym'



class WikiPagesQuerySet(QuerySet):
    pass


class WikiPagesManager(
        Manager.from_queryset(WikiPagesQuerySet)):
    pass


class WikiPagesVersionQuerySet(QuerySet):


    def get_instance_query(self):
        # put some logic to prevent
        # executin from model
        return self.all()

    def get_versions_list(self):
        return self.get_instance_query().order_by('-is_current', 'id')

    def clear_current(self):
        return self.get_instance_query().update(is_current=False)

    def set_current(self, version_id):
        self.clear_current()
        return self.get_instance_query().filter(id=version_id).update(is_current=True)

    def get_current(self):
        return self.filter(is_current=True)


class WikiPagesVersionManager(
        Manager.from_queryset(WikiPagesVersionQuerySet)):
    pass
