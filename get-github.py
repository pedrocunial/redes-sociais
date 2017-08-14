import os

from github import Github


ROOT_NODE = 'tj'

DATA_FOLDER = 'github'


def save_successors(user, successors):
    path = os.path.join(DATA_FOLDER, user.login + '.txt')

    with open(path, 'w', encoding='utf-8') as file:
        for successor in successors:
            file.write(successor.login + '\n')


def main():
  api = Github(
      'SEU LOGIN',
      'SUA SENHA',
  )

  root_user = api.get_user(ROOT_NODE)

  users = root_user.get_following()

  save_successors(root_user, users)

  for user in users:
      print(user.login)

      successors = user.get_following()

      save_successors(user, successors)


if __name__ == '__main__':
    main()
