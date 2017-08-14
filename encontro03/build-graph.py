import os

from unidecode import unidecode


DATA_FOLDER = 'twitter'

ROOT_NODE = 'realDonaldTrump'

ROOT_NAME = 'realDonaldTrump'

ROOT_DEPTH = 1

INCLUDE_ROOT = True

DIRECTED = False

GRAPH_NAME = 'twitter'


def load_successors(node, depth=1, names=None):
    successors = set()

    path = os.path.join(DATA_FOLDER, node + '.txt')

    try:
        with open(path, encoding='utf-8') as file:
            for line in file:
                words = line.split()

                if words:
                    successor = words[0]

                    successors.add(successor)

                    if names is not None and len(words) > 1:
                        names[successor] = unidecode(' '.join(words[1:]))
    except FileNotFoundError:
        pass

    if depth > 1:
        successors_copy = successors.copy()

        for successor in successors_copy:
            successors |= load_successors(node, depth - 1, names)

    return successors


def main():
    nodes = []

    names = {}

    successors = load_successors(ROOT_NODE, ROOT_DEPTH, names)

    successors.discard(ROOT_NODE)

    if INCLUDE_ROOT:
        nodes.append(ROOT_NODE)

        names[ROOT_NODE] = ROOT_NAME

    nodes.extend(successors)

    edges = []

    for i, node in enumerate(nodes):
        successors = load_successors(node)

        for successor in successors:
            try:
                j = nodes.index(successor)
            except ValueError:
                continue

            edges.append((i, j))

    if not DIRECTED:
        edges = [(i, j) for i, j in edges if i < j and (j, i) in edges]

    with open(GRAPH_NAME + '.gml', 'w') as file:
        file.write('graph [\n')
        file.write('  directed {}\n'.format(int(DIRECTED)))

        for i, node in enumerate(nodes):
            file.write('  node [\n')
            file.write('    id {}\n'.format(i))
            if node in names:
                label = names[node]
            else:
                label = node
            file.write('    label "{}"\n'.format(label))
            file.write('  ]\n')

        for i, j in edges:
            file.write('  edge [\n')
            file.write('    source {}\n'.format(i))
            file.write('    target {}\n'.format(j))
            file.write('  ]\n')

        file.write(']\n')


if __name__ == '__main__':
    main()
