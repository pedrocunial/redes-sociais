graph [
  directed 0
  node [
    id 0
    label "D1"
    x 0.5
    y 1.0
  ]
  node [
    id 1
    label "E1"
    x 0.0
    y 0.6
  ]
  node [
    id 2
    label "E2"
    x 1.0
    y 0.6
  ]
  node [
    id 3
    label "F1"
    x 0.0
    y 0.0
  ]
  node [
    id 4
    label "F2"
    x 1.0
    y 0.0
  ]
  edge [
    source 0
    target 1
    strong 1
  ]
  edge [
    source 0
    target 2
    strong 1
  ]
  edge [
    source 1
    target 3
    strong 1
  ]
  edge [
    source 2
    target 4
    strong 1
  ]
  edge [
    source 3
    target 4
    strong 0
  ]
]
