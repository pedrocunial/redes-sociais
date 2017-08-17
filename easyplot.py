import plotly

from math import sqrt, cos, sin


HEAD_ANGLE = 0.5


graph_width = 272
graph_height = 272

point_size = 10
vector_width = 1


def _scale(dx, dy, width, height, size):
    s2 = size**2

    x2 = (dx * width)**2
    y2 = (dy * height)**2

    return sqrt(s2 / (x2 + y2))


def _rotate(dx, dy, width, height, counter):
    dx *= width
    dy *= height

    if counter:
        a = HEAD_ANGLE
    else:
        a = -HEAD_ANGLE

    rx = dx * cos(a) - dy * sin(a)
    ry = dx * sin(a) + dy * cos(a)

    return rx / width, ry / height


def _convert(color):
    return 'rgb({}, {}, {})'.format(color[0], color[1], color[2])


def _build_point_trace(color):
    return {
        'x': [],
        'y': [],
        'hoverinfo': 'none',
        'mode': 'markers',
        'marker': {
            'size': point_size,
            'color': _convert(color),
        },
    }


def _build_vector_trace(color):
    return {
        'x': [],
        'y': [],
        'hoverinfo': 'none',
        'mode': 'lines',
        'line': {
            'width': vector_width,
            'color': _convert(color),
        },
    }


def _build_layout(width, height, xrange, yrange):
    layout = {
        'showlegend': False,
        'width': width,
        'height': height,
        'margin': {
            'b': 0,
            'l': 0,
            'r': 0,
            't': 0,
        },
        'xaxis': {
            'showticklabels': False,
        },
        'yaxis': {
            'showticklabels': False,
        },
    }

    if xrange is not None:
        layout['xaxis']['range'] = xrange

    if yrange is not None:
        layout['yaxis']['range'] = yrange

    return layout


def _add_point(x, y, point_trace):
    point_trace['x'].append(x)
    point_trace['y'].append(y)


def _add_vector(x1, y1, vector_trace):
    x0 = 0
    y0 = 0

    dx = y0 - y1
    dy = x1 - x0

    # parameters estimated from screenshots
    width = 0.9 * graph_width - 24
    height = 0.9 * graph_height - 24

    vector_trace['x'].extend([x0, x1, None])
    vector_trace['y'].extend([y0, y1, None])

    dx = x0 - x1
    dy = y0 - y1

    radius = point_size / 2

    x0 = x1
    y0 = y1

    rx, ry = _rotate(dx, dy, width, height, True)
    scale = _scale(rx, ry, width, height, radius)
    x1 = x0 + rx * scale
    y1 = y0 + ry * scale
    vector_trace['x'].extend([x0, x1, None])
    vector_trace['y'].extend([y0, y1, None])

    rx, ry = _rotate(dx, dy, width, height, False)
    scale = _scale(rx, ry, width, height, radius)
    x1 = x0 + rx * scale
    y1 = y0 + ry * scale
    vector_trace['x'].extend([x0, x1, None])
    vector_trace['y'].extend([y0, y1, None])


def _frame(pairs, colors, build_function, add_function):
    traces = []

    for pair, color in zip(pairs, colors):
        trace = build_function(color)
        traces.append(trace)
        add_function(pair[0], pair[1], trace)

    return {
        'data': traces,
    }


def frame_points(pairs, colors):
    return _frame(pairs, colors, _build_point_trace, _add_point)


def frame_vectors(pairs, colors):
    return _frame(pairs, colors, _build_vector_trace, _add_vector)


def show_animation(frames, xrange=None, yrange=None):
    steps = []

    for index, frame in enumerate(frames):
        frame['name'] = index
        steps.append({
            'args': [[index], {'frame': {'redraw': False}, 'mode': 'immediate'}],
            'label': '',
            'method': 'animate',
        })

    # parameters estimated from screenshots
    width = 1.05 * graph_width + 72
    height = 1.00 * graph_height + 76

    layout = _build_layout(width, height, xrange, yrange)

    layout.update({
        'updatemenus': [
            {
                'buttons': [
                    {
                        'args': [None, {'frame': {'redraw': False}, 'fromcurrent': True}],
                        'label': 'Play',
                        'method': 'animate',
                    },
                    {
                        'args': [[None], {'frame': {'redraw': False}, 'mode': 'immediate'}],
                        'label': 'Pause',
                        'method': 'animate',
                    },
                ],
                'showactive': True,
                'type': 'buttons',
            },
        ],
        'sliders': [
            {
                'currentvalue': {'visible': False},
                'steps': steps,
            },
        ],
    })

    figure = {
        'data': frames[0]['data'],
        'layout': layout,
        'frames': frames,
    }

    plotly.offline.iplot(figure, config={'displayModeBar': False}, show_link=False)


plotly.offline.init_notebook_mode(connected=True)
