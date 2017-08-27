graph [
  directed 0
  node [
    id 0
    label "A"
    x 0.5
    y 0.4
  ]
  node [
    id 1
    label "B1"
    x 0.5
    y 1.0
  ]
  node [
    id 2
    label "B2"
    x 0.0
    y 0.0
  ]
  node [
    id 3
    label "B3"
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
    source 0
    target 3
    strong 1
  ]
  edge [
    source 1
    target 2
    strong 0
  ]
  edge [
    source 1
    target 3
    strong 0
  ]
  edge [
    source 2
    target 3
    strong 0
  ]
]
