setMargin(int)
setContentsMargins(int left, int top, int right, int bottom);
setContentsMargins(const QMargins &margins) 
设置外边距
setMargin可以设置左、上、右、下的外边距，设置之后，他们的外边距是相同的。 
setContentsMargins与其功能相同，但是可以将左、上、右、下的外边距设置为不同的值。

setSpacing(int) 
设置间距

addStretch() 
添加了一个伸缩空间（QSpacerItem）。

在第一个控件之前添加伸缩，这样所有的控件就会居右显示。
在最后一个控件之后添加伸缩，这样所有的控件就会居左显示。
在第一个控件之前、最后一个控件之后添加伸缩，这样所有的控件就会居中显示。
在每一个控件之间都添加伸缩，这样所有的控件之间的间距都会相同。
QHBoxLayout *pHLayout = new QHBoxLayout();
pHLayout->addWidget(pButton1);
pHLayout->addWidget(pButton2);
pHLayout->addWidget(pButton3);
pHLayout->addWidget(pButton4);
pHLayout->addWidget(pButton5);
pHLayout->addStretch();  // 添加伸缩

事件：Event
QWidget.eventFilter()
