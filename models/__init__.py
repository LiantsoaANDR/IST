"""Cree une instance FileStorage pour notre application"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()