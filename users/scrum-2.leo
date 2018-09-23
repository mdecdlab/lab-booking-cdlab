<?xml version="1.0" encoding="utf-8"?>
<!-- Created by Leo: http://leoeditor.com/leo_toc.html -->
<leo_file xmlns:leo="http://leoeditor.com/namespaces/leo-python-editor/1.1" >
<leo_header file_format="2" tnodes="0" max_tnode_index="0" clone_windows="0"/>
<globals body_outline_ratio="0.5" body_secondary_ratio="0.5">
	<global_window_position top="50" left="50" height="500" width="700"/>
	<global_log_window_position top="0" left="0" height="0" width="0"/>
</globals>
<preferences/>
<find_panel_settings/>
<vnodes>
<v t="leo.20180923111315.1"><vh>@settings</vh>
<v t="leo.20180923111315.2"><vh>@data qt-gui-plugin-style-sheet</vh></v>
<v t="leo.20180923111315.3"><vh>@string initial_split_orientation = horizontal</vh></v>
</v>
<v t="leo.20180923111238.2" a="E"><vh>啟動 lab-booking-cdlab 專案</vh>
<v t="leo.20180923111416.1"><vh>users 目錄</vh></v>
<v t="leo.20180923112011.1"><vh>project layout</vh></v>
</v>
<v t="leo.20180923111821.1" a="E"><vh>@path ./../</vh>
<v t="leo.20180923111740.1" a="E"><vh>編輯 .gitignore</vh>
<v t="leo.20180923111806.1"><vh>@edit .gitignore</vh></v>
<v t="leo.20180923124600.1"><vh>@edit MANIFEST.in</vh></v>
<v t="leo.20180923114101.1"><vh>@edit wsgi.py</vh></v>
</v>
<v t="leo.20180923112617.1" a="E"><vh>@path flaskb</vh>
<v t="leo.20180923121736.1" a="E"><vh>以下為 templates 目錄</vh>
<v t="leo.20180923121709.1" a="E"><vh>@path templates</vh>
<v t="leo.20180923122627.1"><vh>@edit base.html</vh></v>
<v t="leo.20180923121907.1" a="E"><vh>@path auth</vh>
<v t="leo.20180923121920.1"><vh>@edit register.html</vh></v>
<v t="leo.20180923122440.1"><vh>@edit login.html</vh></v>
</v>
</v>
</v>
<v t="leo.20180923121819.1"><vh>以下為 static 目錄</vh>
<v t="leo.20180923121718.1"><vh>@path static</vh></v>
</v>
<v t="leo.20180923113004.1"><vh>@edit __init__.py</vh></v>
<v t="leo.20180923114836.1"><vh>@edit db.py</vh></v>
<v t="leo.20180923114932.1"><vh>@edit schema.sql</vh></v>
<v t="leo.20180923121323.1"><vh>@edit auth.py</vh></v>
</v>
</v>
</vnodes>
<tnodes>
<t tx="leo.20180923111238.2"></t>
<t tx="leo.20180923111315.1"></t>
<t tx="leo.20180923111315.2">QSplitter::handle {
    background-color: #CAE1FF; /* lightSteelBlue1 */
}

QStackedWidget {
    /* background-color:lightpink; */
    border-color: red;
    padding: 0px;
    /* border-width: 0px; */
    /* background-color: yellow; */
}

QSplitter {
    border-color: white;
    background-color: white;
    border-style: solid;
}

QTreeWidget {
    /* These apply to the selected item, but not to editing items.*/
    background-color: #ffffec; /* Leo's traditional tree color */
    selection-color: black; /* was white */
    selection-background-color: lightgrey;
    /* font-family: SansSerif; */
    /*font-family: DejaVu Sans Mono;*/
    font-family:YaHei Mono;
    /* 標題字型大小設定 */
    font-size: 20px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal, italic,oblique */
 }

/* Headline edit widgets */
QTreeWidget QLineEdit {
    background-color: cornsilk;
    selection-color: white;
    selection-background-color: blue;
    /*font-family: DejaVu Sans Mono;*/    
    font-family:YaHei Mono;
    /* 沒有特別對應字型大小 */
    font-size: 20px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal, italic,oblique */
}

/* The log panes */
QTextEdit {
    background-color: #f2fdff;
    selection-color: red;
    selection-background-color: blue;
    /* font-family: Courier New; */
    font-family:YaHei Mono;
    /* log font 大小 */
    font-size: 20px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal, italic,oblique */
}

/* The body pane */
QTextEdit#richTextEdit {
    background-color: #fdf5f5; /* A kind of pink. */
    selection-color: white;
    selection-background-color: red;
    /*font-family: DejaVu Sans Mono;*/
    /* font-family: Courier New; */
    font-family:YaHei Mono;
    /* 內文字型大小 */
    font-size: 20px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal,italic,oblique */
}

QLabel {
    font-family:YaHei Mono;
    /* 下方的 Minibuffer 標題字型大小 */
    font-size: 20px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal,italic,oblique */
}

/* Editor labels */
QLineEdit#editorLabel {
    background-color: #ffffec;
    font-family:YaHei Mono;
    /* 沒有直接對應字型大小 */
    font-size: 20px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal,italic,oblique */
    border: 2px;
    margin: 2px;
}</t>
<t tx="leo.20180923111315.3">horizontal: body pane to the left
vertical: body pane on the botton</t>
<t tx="leo.20180923111416.1">為了避免合併 .leo 檔案, 各協同者必須各自在 users 下擁有一個 .leo 檔案

例如: scrum-2 用戶是在管理者修改 lab-booking-cdlab 專案, 移除 settings 管理權限後才加入 cdlab  team 的用戶, 因此不具協同倉儲管理權, 而 scrum-1 則在第一時間加入協同, 因此具備協同倉儲管理權.</t>
<t tx="leo.20180923111740.1"></t>
<t tx="leo.20180923111821.1"></t>
<t tx="leo.20180923112011.1">根據

http://flask.pocoo.org/docs/1.0/tutorial/layout/

設置

flaskb/, a Python package containing your application code and files.

tests/, a directory containing test modules.

It’s time to start coding! Create the flaskb directory and add the __init__.py file. The __init__.py serves double duty: it will contain the application factory, and it tells Python that the flaskb directory should be treated as a package.</t>
<t tx="leo.20180923112617.1"></t>
<t tx="leo.20180923121709.1"></t>
<t tx="leo.20180923121718.1"></t>
<t tx="leo.20180923121736.1"></t>
<t tx="leo.20180923121819.1"></t>
<t tx="leo.20180923121907.1"></t>
</tnodes>
</leo_file>
