import React, { Component } from 'react'
import L from 'react-dom-factories'
L_ = React.createElement

export default Notebook = (props) ->
  addr = 'http://localhost:8888/notebooks/test.ipynb'
  nb_addr = 'notebooks/test.ipynb'
  addr = 'http://localhost:8888/notebooks/'+nb_addr
  L.div className:'widget',
    L.div className:'frame',
      L.iframe
       src:addr
       style:
         position:'relative'
         width:'100%'
         height:'100%'
