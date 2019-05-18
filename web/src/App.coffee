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
  constructor:->
    super()
    @layout = [
        i:'notebook', x:0, y:0, w:4, h:7
      , i:'number', x:0, y:8, w:2, h:3
    ]
    console.log @layout
    @callback_chain = new FuncChainer()

  onWsMessage: (msg)=>
      console.log 'new msg', msg
      @callback_chain.call msg.data
    
  render: ->
    L.div className:'app',
      L_ GridLayout,
        className:'grid'
        cols:6
        rowHeight:30
        width:600
        layout: @layout
        draggableCancel:"input"
        L.div key:'notebook', L_ Notebook
        L.div key:'number',
          L_ Visualiser,
            registerCallback:@callback_chain.append,
            sendCallback:(msg)=>
              console.log @state?ws
              if @state?.ws
                console.log 'sending', msg
                @state.ws.send(msg)
            varname:'test'

      L_ WSwrap,
        onMessage:@onWsMessage
        onConnect: (ws)=>
          console.log "connected",ws
          @setState ws:ws

