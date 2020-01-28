#coding:UTF-8

import brute_force_search as bfs

# ノードのソートに使用するモジュールの関数
from operator import methodcaller

# 幅優先探索(width_first_search)
# openlistはキュー(queue)で表現する


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

    
    # オープンリストが空であるかを返すインスタンスメソッド
    def is_empty(self):
          # 空でないときはFalseを返す
          # 空であるときはTrueを返す
          return False if self.__openlist else True
    # is_empty　終了

    
    # オープンリストの末尾にnode_listを追加するインスタンスメソッド
    # node_listにゴールノードが含まれる場合は先頭に割り込ませる（各自作成）
    def add_node_list(self, node_list, closed):
        
        # node_listから、割り込ませるゴールノードのリストfirstと
        # オープンリストに追加するノードの候補のリストcandidatesを作成する
        first = []
        candidates = 

        
        # 割り込ませるゴールノードのリストをid順でソート
        first.sort(key=methodcaller("id"))

        # node_listからオープンリストにもクローズドリストにも
        # 含まれないノードを抽出する
        open_closed = self.__openlist + closed.elements()
        new_nodes = []

        
                # nodeと同じidのノードelmが既にオープンかクローズドに含まれるならば
        
                    # nodeをnew_nodesに追加する必要はない

                    
            # nodeは実際にオープンにもクローズドにも含まれないならば

            
        # new_nodesをid順でソート
        new_nodes.sort(key=methodcaller("id"))
                
        # オープンリストを更新する（リストを結合する順番に注意）

    # add_node_list　終了

    
    # オープンリストの先頭の要素を返し、内容を更新するインスタンスメソッド
    def get_first(self):
        # 先頭の要素を削除しfirstに確保
        first = self.__openlist.pop(0)
        # openlistの先頭を削除したので、openlistの内容は更新済み
        # firstを返す
        return(first)
    # get_first　終了

    
    # オープンリストの内容を文字列で返すインスタンスメソッド（各自作成）
    def view(self):

        # オープンリストの内容を表す文字列olを返す
        return(ol)
    # view　終了
# オープンリストの定義　終了
