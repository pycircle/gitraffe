#from PyQt4.QtCore import Qt, QAbstractListModel, QModelIndex, QVariant

class Repository():
    def __init__(self, rep_id, name, path):
        self.id = rep_id
        self.name = name
        self.path = path
#===============================================================================
#        
# class Repositories_table(Repository, QAbstractListModel):
#    def __init__(self, rep_id, name, path, parent, *args):
#        Repository.__init__(self, rep_id, name, path)
#        QAbstractListModel.__init__(self, parent, *args)
#        self.listdata = [rep_id, name, path]
#    def rowCount(self, parent=QModelIndex()): 
#        return len(self.listdata)
#    def data(self, index, role): 
#        if index.isValid() and role == Qt.DisplayRole:
#            return QVariant(self.listdata[index.row()])
#        else: 
#            return QVariant()
#===============================================================================