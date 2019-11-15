import React, { Component } from 'react'
import L from 'react-dom-factories'
L_ = React.createElement

import GridLayout from 'react-grid-layout'
#import ResponsiveGL from 'react-grid-layout'
import {Responsive, WidthProvider} from 'react-grid-layout'
import Notebook from './modules/notebook.coffee'
import Visualiser from './modules/visualiser.coffee'
import WSwrap from './modules/ws.coffee'

import Button from './modules/UIcomponents/button.coffee'

import FuncChainer from './modules/helpers/funchainer.coffee'
import {get_nb_name} from './modules/helpers/argparser.coffee'

import './styles/grid.css'
import './styles/widget.less'
import './styles/graph.less'
import './styles/misc.less'

ResponsiveGL = WidthProvider( Responsive)

_get_layout=(vars)->
  layout = [
      i:'notebook', x:0, y:0, w:4, h:7
  ]

  for v, idx in vars
    layout.push i:'vis'+idx, x:2*(idx%2), y:7+4*idx, w:2, h:4
  return layout

export default class App extends React.Component
  state:
    vars: [
      #name:'test', value:'asss' 
       name:'image', value:'asss'
    ]
  constructor:->
    super()
    @state.layout = _get_layout(@state.vars)

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

  add_widget: ()=>
    @setState (s,p)->
      new_var = name:'New',value:'Not init'
      s.layout.push _get_layout new_var
      s.vars.push new_var
      s

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
      L.div className:'top-bar',
        L_ WSwrap,
          className:'inline'
          onMessage:@onWsMessage
          onConnect: @onConnect
          onDisconnect: @onDisconnect
        L_ Button,
          className:'add-widget'
          text:'Add widget'
          onPress:@add_widget
      L_ ResponsiveGL,
        className:'grid'
        cols:12
        rowHeight:60
        width:1000
        layouts: @state.layout
        breakpoints:{lg: 1200, md: 996, sm: 768, xs: 480, xxs: 0}
        cols:{lg: 18, md: 12, sm: 10, xs: 4, xxs: 2}
        draggableCancel:"input"
        L.div key:'notebook', L_ Notebook, nb_name:get_nb_name()
        for v,idx in @state.vars
          L.div key:'vis'+idx,
            L_ Visualiser,
              value:v.value
              varname:v.name
              type:v.type
              onNameChange:@nameChange idx
