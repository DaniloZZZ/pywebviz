import React, { Component } from 'react'
import L from 'react-dom-factories'
L_ = React.createElement

export default Notebook = (props) ->
  L.div className:'widget',
    L.iframe
     src:'http://localhost:8888/notebooks/test.ipynb'
     style:
       position:'relative'
       width:'100%'
       height:'100%'


