import click
from git import Repo
import os

repo = None


def clone_repo(source_repo, target_path='./repo'):
    # os.makedirs(target_path)
    Repo.clone_from(source_repo, target_path)


@click.command()
@click.argument('source_repo', required=True)
def main(source_repo):
    clone_repo(source_repo)


if __name__ == '__main__':
    main()
