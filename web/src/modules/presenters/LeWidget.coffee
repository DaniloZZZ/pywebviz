import React, { Component } from 'react'
import L from 'react-dom-factories'
L_ = React.createElement

import LeClient from 'legimens'
import {choosePresenter} from '../visualiser.coffee'

export default LeWidget = ({data, addr})->
  L.div null,
    L_ LeClient, addr:addr, refval:data,
      (variable, setattr) =>
        if variable is undefined
          variable = value:'Loading', type:'raw'
        else
          variable = JSON.parse variable
        console.log('in le_widget choosePresenter', variable)
        Pres = choosePresenter variable.type, variable
        L_ Pres, data:variable, addr:addr

