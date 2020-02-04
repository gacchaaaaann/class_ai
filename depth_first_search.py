#coding:UTF-8

import brute_force_search as bfs

# ノードのソートに使用するモジュールの関数
from operator import methodcaller

# 深さ優先探索(depth_first_search)
# openlistはスタック(stack)で表現する


# オープンリストの定義
class OpenList:
    # rootノードを作成しこれのみを含むようにオープンリストを初期化
    def __init__(self):
        root = bfs.Node(bfs.ROOT_NODE, bfs.ROOT_PARENT)
        self.__openlist = [root]
    # __init__終了

    
    # オープンリストの内容を返すインスタンスメソッド
    def elements(self):
        return(self.__openlist)
    # elements　終了

    
    # オープンリストが空であるかを返すインスタンスメソッド（各自作成）
    def is_empty(self):
        return not self.__openlist
    # is_empty　終了

    
    # オープンリストの先頭にnode_listを追加するインスタンスメソッド
    # ゴールノードはオープンリストの先頭に割り込ませる
    def add_node_list(self, node_list, closed):
        # node_listから、割り込ませるゴールノードのリストtopと
        # オープンリストに追加するノードの候補のリストcandidatesを作成する
        top = []
        candidates = []

        for node in node_list:
            if node.id() >= bfs.GOAL_THRESHOLD:
                top.append(node)
            else:
                candidates.append(node)


        top.sort()

        # candidatesからオープンリストにもクローズドリストにも
        # 含まれないノードを抽出する
        open_closed = self.__openlist + closed.elements()
        new_nodes = []

        for node in candidates:
            for elm in open_closed:
                # nodeと同じidのノードelmが既にオープンかクローズドに含まれるならば
                if elm.id() == node.id():
                    # nodeをnew_nodesに追加する必要はない
                    break

            # nodeは実際にオープンにもクローズドにも含まれないならば
            else:
                new_nodes.append(node)
                continue

            
        # ノードのid順でソート
        new_nodes.sort(key=methodcaller("id"))
                
        # 「スタックに積む」ことでオープンリストを更新する（順番に注意）
        self.__openlist = top + new_nodes + self.__openlist

    # add_node_list　終了

    
    # オープンリストの先頭の要素を返し、内容を更新するインスタンスメソッド
    def get_first(self):
        # 先頭の要素を削除しfirstに確保
        first = self.__openlist.pop(0)
        # openlistの先頭を削除したので、openlistの内容は更新済み
        # firstを返す
        return(first)
    # get_first　終了

    
    # オープンリストの内容を文字列で返すインスタンスメソッド
    def view(self):
        
        ol = "( "
        b = False   #間に,を入れるため，ノード数と,を入れる処理の回数に1の差gが発生するため，初回のみ処理を別にする必要があり，そのためのフラグ

        for node in self.__openlist:    #表示を簡潔にわかりやすくするため，表示すべきはidのみで良いと判断した(理由:idに一意性がある)
            if b:
                ol += "," + str(node.id())

            else:
                ol += str(node.id())
                b = True

        ol += " )"
        
        return(ol)
    # view　終了
# オープンリストの定義　終了
