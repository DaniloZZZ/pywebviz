import LeClient from 'legimens'
import L from 'react-dom-factories'
import React, { Component } from 'react'
L_ = React.createElement

export Widget = ({refval, addr, children})=>
  <LeClient addr={addr} refval={refval}>
    { (variable, setattr) =>
        L.div
          className:'container'
          L_ children, variable, setattr
    }
  </LeClient>

import ResponsiveGL from './modules/ResponsiveStorageGrid.coffee'
export GridLayout = ResponsiveGL

