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

    # is_empty　終了

    
    # オープンリストの先頭にnode_listを追加するインスタンスメソッド
    # ゴールノードはオープンリストの先頭に割り込ませる
    def add_node_list(self, node_list, closed):
        # node_listから、割り込ませるゴールノードのリストtopと
        # オープンリストに追加するノードの候補のリストcandidatesを作成する
        top = []
        candidates = []

        top.sort()

        # candidatesからオープンリストにもクローズドリストにも
        # 含まれないノードを抽出する
        open_closed = self.__openlist + closed.elements()
        new_nodes = []

                # nodeと同じidのノードelmが既にオープンかクローズドに含まれるならば

                    # nodeをnew_nodesに追加する必要はない

                    
            # nodeは実際にオープンにもクローズドにも含まれないならば

            
        # ノードのid順でソート
        new_nodes.sort(key=methodcaller("id"))
                
        # 「スタックに積む」ことでオープンリストを更新する（順番に注意）

        
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
        
        return(ol)
    # view　終了
# オープンリストの定義　終了
