import React, { Component } from 'react';

class SvgIconsPopUp extends Component {
  // Метод для отрисовки иконки крестика
  renderCloseIcon = (color = 'white', size = 24) => {
    return (
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fillRule="evenodd" clipRule="evenodd" d="M6.21875 6.21875C6.51043 5.92708 6.98333 5.92708 7.27497 6.21875L11.5 10.4438L15.725 6.21875C16.0167 5.92708 16.4895 5.92708 16.7813 6.21875C17.0729 6.51043 17.0729 6.98333 16.7813 7.27497L12.5562 11.5L16.7813 15.725C17.0729 16.0167 17.0729 16.4895 16.7813 16.7813C16.4895 17.0729 16.0167 17.0729 15.725 16.7813L11.5 12.5562L7.27497 16.7813C6.98333 17.0729 6.51043 17.0729 6.21875 16.7813C5.92708 16.4895 5.92708 16.0167 6.21875 15.725L10.4438 11.5L6.21875 7.27497C5.92708 6.98333 5.92708 6.51043 6.21875 6.21875Z" fill="black"/>
        </svg>
    );
  }

    render() {
        const { iconName, color, size } = this.props;

        switch(iconName) {
            case 'close':
                return this.renderCloseIcon(color, size);
            default:
                return null;
        }
    }

}

export default SvgIconsPopUp;
