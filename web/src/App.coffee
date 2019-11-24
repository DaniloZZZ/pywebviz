import React, { Component } from 'react'
import L from 'react-dom-factories'
L_ = React.createElement

import Notebook from './modules/notebook.coffee'
import Visualiser from './modules/visualiser.coffee'
import WSwrap from './modules/ws.coffee'
import ResponsiveGL from './modules/ResponsiveStorageGrid.coffee'
import {Responsive, WidthProvider} from 'react-grid-layout'

import Button from './modules/UIcomponents/button.coffee'
import Widget from './modules/Widget.coffee'

import FuncChainer from './modules/helpers/funchainer.coffee'
import LocalStorage from './modules/helpers/localStorage.coffee'
import {get_nb_name} from './modules/helpers/argparser.coffee'

import './styles/grid.css'
import './styles/widget.less'
import './styles/graph.less'
import './styles/misc.less'

visStorage = new LocalStorage key:'webvis'

defaultVars = [
      #name:'test', value:'asss' 
       name:'image', value:'asss'
    ]

export default class App extends React.Component
  state: {}
  constructor:->
    super()
    @state.vars = visStorage.get('vars') or defaultVars

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
    new_var = name:'New variable',value:'Nothing here yet'
    @setState (s,p)->
      s.vars.push new_var
      visStorage.save 'vars', s.vars
      s
  deleteWidget: (id)->()=>
    @setState (s,p)->
      s.vars.pop id
      visStorage.save 'vars', s.vars
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

  wrap: (props)->
    L.div '',
      props.children
  
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
        draggableCancel:"input"
        L.div key:'notebook', L_ Notebook, nb_name:get_nb_name()
        for v,idx in @state.vars
          Widget
            onDelete:@deleteWidget idx
            key:'vis'+idx
            L.div key:'vis'+idx,
              L_ Visualiser,
                value:v.value
                varname:v.name
                type:v.type
                onNameChange:@nameChange idx
