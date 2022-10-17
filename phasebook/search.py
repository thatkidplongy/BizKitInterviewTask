from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    if not args:
        return USERS
    
    else:
        filters = []
        print(args)
        id = args.get('id')
        name = args.get('name')
        age = args.get('age')
        occupation = args.get('occupation')
         
        for user in USERS:

            if id:
                if args['id'] == user['id']:
                    filters.append(user)
            
            if name:
                if args['name'].lower() in user['name'].lower():
                    filters.append(user)
            
            if age:
                age = int(age)
                if user['age'] in range((age-1), (age+2)):
                    filters.append(user)
            
            if occupation:
                if args['occupation'].lower() in user['occupation'].lower():
                    filters.append(user)

        filters = [dict(tuple) for tuple in {tuple(filter.items()) for filter in filters}]

        filters = sorted(filters, key=lambda filter: (filter['id'], filter['name'], filter['age'], filter['occupation']))

        return filters
