import React, { Component } from 'react'
import L from 'react-dom-factories'
L_ = React.createElement

import GridLayout from 'react-grid-layout'
#import ResponsiveGL from 'react-grid-layout'
import {Responsive, WidthProvider} from 'react-grid-layout'
import Notebook from './modules/notebook.coffee'
import Visualiser from './modules/visualiser.coffee'
import WSwrap from './modules/ws.coffee'

import FuncChainer from './modules/helpers/funchainer.coffee'

import './styles/grid.css'
import './styles/widget.less'
import './styles/graph.less'

ResponsiveGL = WidthProvider( Responsive)

export default class App extends React.Component
  state:
    vars: [
      #name:'test', value:'asss' 
       name:'image', value:'asss'
    ]
  constructor:->
    super()
    @layout = [
        i:'notebook', x:0, y:0, w:4, h:7
    ]
    for v,idx in @state.vars
      @layout.push i:'vis'+idx, x:2*(idx%2), y:7+4*idx, w:2, h:4

    @responsive_layout = lg:@layout

  onWsMessage: (msg)=>
      jsonser = msg.data
      if jsonser == "None"
        return

      # do not update if not changed
      for v in @state.vars
        if v.string==jsonser
          return
      @setState (s,p)->
        try
          message = JSON.parse jsonser
        catch
          message = jsonser
          console.error message
          return s
        name = message.args
        value = message.value
        type = message.type
        for v in s.vars
          if v.name==name
            v.value = value
            v.type = type
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
        ws.send 'get:'+v.name
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
      L_ ResponsiveGL,
        className:'grid'
        cols:12
        rowHeight:60
        width:1000
        layouts: @responsive_layout
        breakpoints:{lg: 1200, md: 996, sm: 768, xs: 480, xxs: 0}
        cols:{lg: 18, md: 12, sm: 10, xs: 4, xxs: 2}
        draggableCancel:"input"
        L.div key:'notebook', L_ Notebook
        for v,idx in @state.vars
          L.div key:'vis'+idx,
            L_ Visualiser,
              value:v.value
              varname:v.name
              type:v.type
              onNameChange:@nameChange idx
