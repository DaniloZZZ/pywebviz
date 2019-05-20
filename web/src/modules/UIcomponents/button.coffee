import L from 'react-dom-factories'

import './button.less'

export default Button = (props)->
    L.div
      className:'ui-button'
      onClick:props.onPress
      props.text

