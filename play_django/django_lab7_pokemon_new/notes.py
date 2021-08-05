# # pokemon!

# # remember delimeters
# # remember CSRF token!
# # is it necessary to have the Vue script inside the django html file, or can it be loaded in static no big deal?

# for the new pokemon, see wed 4 aug's example of new post Vue form to interact with API:
    # #vue methods
    # load pokemon
        # vue created hook: this.loadpokemon()
    # create pokemon, axios request
    # method POST, same URL, headers csrf token 'X-CSRFToken': 
        # add line in function let csrf_token = document.queryS...

    # 
# in his example, the user list was hardcoded in, should only be applicable users...


# api_app / router.urls ...
    # add a view current user view to get the current user class based
    # add loadCurrentUser() to methods in vue