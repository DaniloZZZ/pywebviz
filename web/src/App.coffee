import React, { Component } from 'react'
import L from 'react-dom-factories'
L_ = React.createElement

import {Responsive, WidthProvider} from 'react-grid-layout'

import LeClient from 'legimens'

import Notebook from './modules/notebook.coffee'
import Visualiser from './modules/visualiser.coffee'
import WSwrap from './modules/ws.coffee'
import ResponsiveGL from './modules/ResponsiveStorageGrid.coffee'
import Widget from './modules/Widget.coffee'
import Input from './modules/UIcomponents/input.coffee'
import Button from './modules/UIcomponents/button.coffee'

import FuncChainer from './modules/helpers/funchainer.coffee'
import LocalStorage from './modules/helpers/localStorage.coffee'
import {get_nb_name} from './modules/helpers/argparser.coffee'
import {parse_message} from './Data/interface.coffee'

import './styles/grid.css'
import './styles/widget.less'
import './styles/graph.less'
import './styles/misc.less'
import './styles/top_bar.less'

visStorage = new LocalStorage key:'webvis'


export default class App extends React.Component
  state: {
    addr:'ws://localhost:7700/'
  }
  constructor:->
    super()
    @state.widgets = visStorage.get('widgets') or {}

  set_widgets:(widgets)->
    @setState {widgets}
    visStorage.save 'widgets', widgets

  nameChange: (id)=>(name)=>
    console.log 'namechange',@state.widgets
    @state.widgets[id].name = name
    @set_widgets @state.widgets

  addWidget: ()=>
    new_widget = name:'New'
    new_id = Date.now()
    @state.widgets[new_id] = new_widget
    @set_widgets @state.widgets

  deleteWidget: (id)->()=>
    console.log "Deleting widget #{id}"
    delete @state.widgets[id]
    @set_widgets @state.widgets

  widget: (v, name, idx) =>
    Widget
      key: idx
      onDelete:@deleteWidget idx
      L_ Visualiser,
        onNameChange:@nameChange idx
        name: name
        variable: v
        addr: @state.addr

  dataWidget:(refval, name, idx)=>
      L.div key:idx,
        L_ LeClient, addr:@state.addr, refval:refval,
          (data, setattr) =>
            if data is undefined
              data = value:'Loading',type:'raw'
              return @widget data, name, idx
            data = JSON.parse data
            @widget data, name, idx
 
  get_widgets:(root)=>
    nb = L.div key:'notebook', L_ Notebook, nb_name:get_nb_name()

    widgets = []
    for idx, params of @state.widgets
      {name} = params
      variable = root?[name]
      if variable is undefined
        v = value:'No such value',type:'raw'
        widgets.push @widget v, name, idx
        continue
      
      widgets.push @widget variable, name, idx
    return [nb, widgets...]

  topbar:(addr)=>
    L.div className:'top-bar',
      L.div className:'address inline',
        L_ Input,
          value: addr
          onChange: (addr)=>@setState {addr}
      L_ Button,
        className: 'add-widget'
        text: 'Add widget'
        onPress: @addWidget

  grid:(vars)->
    L_ ResponsiveGL,
      className:'grid'
      draggableCancel:"input"
      @get_widgets vars

  render: ->
    {addr} = @state
    L.div className:'app',
      @topbar addr
      L_ LeClient, addr:addr, refval:'',
      (root, setattr) =>
        console.log 'root ref', root
        if not root
          return @grid()
        L_ LeClient, addr:addr, refval:root,
          (vars, setattr) =>
            if not vars
              return 'Loading...'
            vars = JSON.parse vars
            @grid vars


