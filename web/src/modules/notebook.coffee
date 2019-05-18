import React, { Component } from 'react'
import L from 'react-dom-factories'
L_ = React.createElement

export default Notebook = (props) ->
  return L.div style:width:'100%',height:'100%',
    L.iframe
     src:'http://localhost:8888/notebooks/test.ipynb'
     style:
       width:'100%'
       height:'100%'


