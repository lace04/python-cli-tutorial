import json_manager
import click

# TODO: Implement the cli group
@click.group()
def cli():
    pass

# TODO: Implement the new, user, delete, update and users commands
@cli.command()
@click.option('--name', prompt='Your name', required=True, help='The person to greet.')
@click.option('--lastname', prompt='Your lastname', required=True, help='The person to greet.')
@click.pass_context
def new(ctx, name, lastname):
  if not name or not lastname:
    ctx.fail('You must provide a name and lastname')
  else:
    data = json_manager.read_json()
    new_id = len(data) + 1
    new_user = {
      'id': new_id,
      'name': name,
      'lastname': lastname
    }
    data.append(new_user)
    json_manager.write_json(data)
    print(f"User {name} {lastname} added successfully with id {new_id}")

@cli.command()
@click.argument('id', type=int)
def user(id):
  data = json_manager.read_json()
  user = next((x for x in data if x['id'] == id), None)
  if user is None:
    print(f"User with id {id} not found")
  else:
    print(f"{user['id']} - {user['name']} - {user['lastname']}")

@cli.command()
@click.argument('id', type=int)
def delete(id):
  data = json_manager.read_json()
  user = next((x for x in data if x['id'] == id), None)
  if user is None:
    print(f"User with id {id} not found")
  else:
    data.remove(user)
    json_manager.write_json(data)
    print(f"User with id {id} deleted successfully")

@cli.command()
@click.argument('id', type=int)
@click.option('--name', prompt='Your name', required=True, help='The person to greet.')
@click.option('--lastname', prompt='Your lastname', required=True, help='The person to greet.')
def update(id, name, lastname):
  if not name or not lastname:
    ctx.fail('You must provide a name and lastname')
  else:
    data = json_manager.read_json()
    user = next((x for x in data if x['id'] == id), None)
    if user is None:
      print(f"User with id {id} not found")
    else:
      user['name'] = name
      user['lastname'] = lastname
      json_manager.write_json(data)
      print(f"User with id {id} updated successfully")

@cli.command()
def users():
    users = json_manager.read_json()
    for user in users:
      print(f"{user['id']} - {user['name']} - {user['lastname']}")

# TODO: Implement the main function
if __name__ == '__main__':
    cli()
