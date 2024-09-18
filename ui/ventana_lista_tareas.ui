<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>474</width>
    <height>337</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <property name="toolTip">
   <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;&lt;br/&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(199, 199, 199)</string>
  </property>
  <layout class="QGridLayout" name="gridLayout">
   <item row="0" column="0" colspan="2">
    <widget class="QLineEdit" name="ingreso_tarea">
     <property name="toolTip">
      <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;&lt;span style=&quot; font-weight:700;&quot;&gt;&lt;br/&gt;&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignmentFlag::AlignCenter</set>
     </property>
     <property name="placeholderText">
      <string>Agregar nueva tarea</string>
     </property>
    </widget>
   </item>
   <item row="0" column="2">
    <widget class="QPushButton" name="boton_agregar_tarea">
     <property name="text">
      <string>Agregar tarea</string>
     </property>
     <property name="autoDefault">
      <bool>false</bool>
     </property>
     <property name="default">
      <bool>false</bool>
     </property>
     <property name="flat">
      <bool>false</bool>
     </property>
    </widget>
   </item>
   <item row="1" column="0">
    <layout class="QGridLayout" name="gridLayout_4">
     <item row="0" column="0" alignment="Qt::AlignmentFlag::AlignHCenter">
      <widget class="QLabel" name="labelTarea">
       <property name="text">
        <string>Tareas</string>
       </property>
      </widget>
     </item>
     <item row="1" column="0">
      <widget class="QTableView" name="tableTareaVacia"/>
     </item>
    </layout>
   </item>
   <item row="1" column="1" colspan="2">
    <layout class="QGridLayout" name="gridLayout_5">
     <item row="0" column="0" alignment="Qt::AlignmentFlag::AlignHCenter">
      <widget class="QLabel" name="labelTareasCompletadas">
       <property name="text">
        <string>Tareas completadas</string>
       </property>
      </widget>
     </item>
     <item row="1" column="0">
      <widget class="QTableView" name="tableTareaCompletada">
       <property name="font">
        <font>
         <strikeout>true</strikeout>
        </font>
       </property>
      </widget>
     </item>
    </layout>
   </item>
   <item row="2" column="0">
    <widget class="QPushButton" name="boton_completar_tarea">
     <property name="text">
      <string>Marcar como completada</string>
     </property>
    </widget>
   </item>
   <item row="2" column="2">
    <widget class="QPushButton" name="boton_eliminar_tarea">
     <property name="text">
      <string>Eliminar</string>
     </property>
    </widget>
   </item>
  </layout>
 </widget>
 <resources/>
 <connections>
  <connection>
   <sender>boton_eliminar_tarea</sender>
   <signal>clicked()</signal>
   <receiver>tableTareaVacia</receiver>
   <slot>clearSelection()</slot>
   <hints>
    <hint type="sourcelabel">
     <x>394</x>
     <y>307</y>
    </hint>
    <hint type="destinationlabel">
     <x>179</x>
     <y>189</y>
    </hint>
   </hints>
  </connection>
 </connections>
</ui>
