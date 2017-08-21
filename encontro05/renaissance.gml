graph [
  directed 0
  node [
    id 0
    label "ginori"
    x 0.5138211382113821
    y 1.0
  ]
  node [
    id 1
    label "lambertes"
    x 0.9658536585365853
    y 0.8673469387755102
  ]
  node [
    id 2
    label "albizzi"
    x 0.5609756097560976
    y 0.736734693877551
  ]
  node [
    id 3
    label "guadagni"
    x 0.8097560975609757
    y 0.6714285714285715
  ]
  node [
    id 4
    label "pazzi"
    x 0.0
    y 0.5061224489795919
  ]
  node [
    id 5
    label "salviati"
    x 0.23414634146341465
    y 0.48367346938775513
  ]
  node [
    id 6
    label "medici"
    x 0.44552845528455287
    y 0.4285714285714286
  ]
  node [
    id 7
    label "tornabuon"
    x 0.6130081300813008
    y 0.5326530612244897
  ]
  node [
    id 8
    label "bischeri"
    x 1.0
    y 0.44897959183673475
  ]
  node [
    id 9
    label "ridolfi"
    x 0.624390243902439
    y 0.33673469387755106
  ]
  node [
    id 10
    label "acciaiuol"
    x 0.26991869918699185
    y 0.2204081632653061
  ]
  node [
    id 11
    label "strozzi"
    x 0.8357723577235773
    y 0.2020408163265306
  ]
  node [
    id 12
    label "peruzzi"
    x 0.9951219512195122
    y 0.17755102040816328
  ]
  node [
    id 13
    label "barbadori"
    x 0.5138211382113821
    y 0.09999999999999998
  ]
  node [
    id 14
    label "castellan"
    x 0.7626016260162601
    y 0.0
  ]
  edge [
    source 0
    target 2
    label "ginori -> albizzi"
  ]
  edge [
    source 2
    target 3
    label "albizzi -> guadagni"
  ]
  edge [
    source 3
    target 1
    label "guadagni -> lambertes"
  ]
  edge [
    source 2
    target 6
    label "albizzi -> medici"
  ]
  edge [
    source 3
    target 7
    label "guadagni -> tornabuon"
  ]
  edge [
    source 7
    target 6
    label "tornabuon -> medici"
  ]
  edge [
    source 6
    target 5
    label "medici -> salviati"
  ]
  edge [
    source 5
    target 4
    label "salviati -> pazzi"
  ]
  edge [
    source 8
    target 3
    label "bischeri -> guadagni"
  ]
  edge [
    source 8
    target 12
    label "bischeri -> peruzzi"
  ]
  edge [
    source 8
    target 11
    label "bischeri -> strozzi"
  ]
  edge [
    source 11
    target 9
    label "strozzi -> ridolfi"
  ]
  edge [
    source 9
    target 7
    label "ridolfi -> tornabuon"
  ]
  edge [
    source 9
    target 6
    label "ridolfi -> medici"
  ]
  edge [
    source 6
    target 10
    label "medici -> acciaiuol"
  ]
  edge [
    source 6
    target 13
    label "medici -> barbadori"
  ]
  edge [
    source 13
    target 14
    label "barbadori -> castellan"
  ]
  edge [
    source 14
    target 11
    label "castellan -> strozzi"
  ]
  edge [
    source 12
    target 14
    label "peruzzi -> castellan"
  ]
]
