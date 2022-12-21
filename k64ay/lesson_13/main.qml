import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 600
    height: 500
    title: "HelloApp"

    TextEdit {
        id: edit
        width: parent.width
        focus: true
        wrapMode: TextEdit.Wrap
        
            }
    Item {
            focus: true
            Keys.onPressed: (event) => {
                console.log(event)
                if ((event.key == Qt.Key_Enter) && (event.modifiers & Qt.ShiftModifier)) {
                    console.log('CTRL+ENTER')
                }
            }
        }


}
