import React, { Component } from 'react'
import L from 'react-dom-factories'
L_ = React.createElement

import GridLayout from 'react-grid-layout'
import Notebook from './modules/notebook.coffee'
import Visualiser from './modules/visualiser.coffee'
import WSwrap from './modules/ws.coffee'

import FuncChainer from './modules/helpers/funchainer.coffee'

import './styles/grid.css'
import './styles/widget.less'

export default class App extends React.Component
  state:
    vars: [
        name:'test', value:'asss'
      , name:'undefined', value:'asss'
    ]
  constructor:->
    super()
    @layout = [
        i:'notebook', x:0, y:0, w:4, h:7
    ]
    for v,idx in @state.vars
      @layout.push i:'vis'+idx, x:2*(idx%2), y:7+4*idx, w:2, h:4

  onWsMessage: (msg)=>
      [name, jsonser] = msg.data.split(":")
      value = JSON.parse jsonser

      for v in @state.vars
        if v.name==name
          if v.string==jsonser
            return
      @setState (s,p)->
        for v in s.vars
          if v.name==name
            v.value = value
            v.string = jsonser


  nameChange: (id)->(name)=>
      @setState (s,p)->
        s.vars[id].name = name
        s
      console.log @state

  onConnect:(ws)=>
    @connected = true
    f= ()=>
      for v in @state?.vars
        ws.send 'getvar:'+v.name
      if @connected
        setTimeout f, 100
    f()
  onDisconnect:()=>
    @connected = false
  
  render: ->
    L.div className:'app',
      L_ WSwrap,
        onMessage:@onWsMessage
        onConnect: @onConnect
        onDisconnect: @onDisconnect
      L_ GridLayout,
        className:'grid'
        cols:6
        rowHeight:30
        width:1000
        layout: @layout
        draggableCancel:"input"
        L.div key:'notebook', L_ Notebook
        for v,idx in @state.vars
          L.div key:'vis'+idx,
            L_ Visualiser,
              value:v.value
              varname:v.name
              onNameChange:@nameChange idx


