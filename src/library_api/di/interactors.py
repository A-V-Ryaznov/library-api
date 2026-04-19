from dishka import Provider, Scope, provide_all

from library_api.application.books.create import CreateNewBookInteractor
from library_api.application.books.get_all import GetAllBooksInteractor
from library_api.application.books.get_by_name import GetBookByNameInteractor
from library_api.application.users.create import CreateNewUserInteractor
from library_api.application.users.get_all import GetAllUsersInteractor


class InteractorsProvider(Provider):
    scope = Scope.REQUEST

    interactors = provide_all(
        CreateNewBookInteractor,
        GetBookByNameInteractor,
        GetAllBooksInteractor,
        GetAllUsersInteractor,
        CreateNewUserInteractor,

    )
