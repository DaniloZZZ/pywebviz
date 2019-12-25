export {default as LineGraph} from './lineGraph_recharts.coffee'
export {default as Image} from './image.coffee'
export {default as MplD3} from './mpld3.coffee'
export {default as Raw} from './Raw.coffee'
export {default as VisVar} from './LeWidget.coffee'

import {wrapLeWidget} from "./LeWidget.coffee"

// installed modules, generated automatically
installed = require('installed')
//import * as installed from "installed"

var x = {}

for (let key of Object.keys(installed)) {
    x[key] = wrapLeWidget( installed[key] );
    console.log(x)
    }
export {x as installed}
