#coding:UTF-8

# Aアルゴリズム(A_algorithm)での
# ノード、オープンリスト、クローズドリスト、状態空間を本ファイルで定義する

# オープンリストのソートに使用するモジュールの関数
from operator import methodcaller

# ルートノードのIDは0
ROOT_NODE = 0
# ルートノードの親ノード（存在しない）のIDは便宜上-1とする
ROOT_PARENT = -1
# 便宜上、ノードIDが1000以上のノードはゴールノードとみなす
GOAL_THRESHOLD = 1000

# ノード(Node)の定義
class Node:
    # 状態空間から得られたノード情報と親ノードを用いて新たなノードを作成する
    def __init__(self, id, parent, g_hat, h_hat):
        self.__param = [id, parent, g_hat, h_hat]
    # __init__終了

    
    # ノードのidを返すインスタンスメソッド
    def id(self):
        return(self.__param[0])
    # id　終了
    
    # ノードの親ノードのidを返すインスタンスメソッド
    def parent(self):
        return(self.__param[1])
    # parent　終了

    # ノードに至る順路の評価値g_hatを返すインスタンスメソッド
    def g_hat(self):

    # g_hat 終了

    # ノードからゴールまでのヒューリスティック評価値h_hatを返すインスタンスメソッド
    def h_hat(self):

    # h_hat終了

    # ノードの評価値の推定値f_hatを返すインスタンスメソッド（f_hatの定義に注意）
    def f_hat(self):

    # f_hat終了
    
    # ノードの内容を返すインスタンスメソッド
    def elements(self):
        return((self.id(),self.parent(),self.g_hat(),self.h_hat()))
    # elements　終了

    # ノードの内容を文字列で返すインスタンスメソッド
    def view(self):
        if self.id() == ROOT_NODE:
            name = "S"
        elif self.id() >= GOAL_THRESHOLD:
            name = "G" + str(self.id()-GOAL_THRESHOLD+1)
        # idが1から6の場合
        elif self.id() <= ord('G') - ord('A'):
            name = chr(ord('A') + self.id() - 1)
        # idが7以降の場合
        else:
            name = chr(ord('A') + self.id())
        # ノードの名前と評価値f_hatを表示
        nd = "(" + name + ", " + str(self.f_hat()) +  ")"
        return(nd)
    # view　終了

    
    # ノードがゴールノードかを判定するインスタンスメソッド
    def is_goal(self):
        if self.id() >= GOAL_THRESHOLD:
            return(True)  # ゴールノードである
        else:
            return(False) # ゴールノードでない
    # is_goal 終了

    
    # 状態空間stを用いて、ノードから到達できる次のノードのリストを得る
    # インスタンスメソッド
    def expand(self, st):
        # 次のノード情報のリストを初期化
        next = []
        next_info = st.next(self.id())
        # 次のノードを作成しnextに追加
        for ni in next_info:
            # 次のノードnnodeはどう初期化すればよいか？
            

            next.append(nnode)

        return(next)
    # expand 終了

    
    # クローズドリストclを用いて、ルートノードから現在のノードに至る
    # 探索されたパスを得るインスタンスメソッド
    def searched_path(self, cl):
        searched = self
        sp = [searched]  # selfは探索されたパスの最後のノード

        # クローズドリストclを逆順にする
        cl.elements().reverse()

        # clに後から追加されたノードから調べる
        for node in cl.elements():
            # searchedノードの親ノードがnodeノードであれば
            if node.id() == searched.parent():
                # nodeは探索されたパスに出現する
                sp.append(node)
                # nodeが次のsearchedになる
                searched = node

        # 調査が終了したら、spを逆順にしてルートから始まるようにする
        sp.reverse()
        # クローズドリストを元の順番に戻す
        cl.elements().reverse()
        
        return(sp)
    # searched_path　終了

    
    # 探索されたパスの内容を文字列で返すインスタンスメソッド
    def view_searched_path(self, sp):

        return(strsp)        
    # view_searched_path　終了
# ノードの定義　終了


#　オープンリストの定義
class OpenList:
    # オープンリストをルートノードのみ含むリストで初期化
    def __init__(self):
        root = Node(ROOT_NODE, ROOT_PARENT, 0, 0)
        self.__openlist = [root]
    # __init__　終了

    
    # オープンリストの内容を返すインスタンスメソッド
    def elements(self):
        return(self.__openlist)
    # elements　終了

    
    # オープンリストが空であるかを返すインスタンスメソッド

    # is_empty　終了
    
    
    # オープンリストに展開で得られたノードnodeを追加
    def add(self, node):
        self.__openlist.append(node)
    # add　終了

    
    # オープンリストの内容を文字列で返すインスタンスメソッド
    def view(self):

        
        return(cl)
    # view　終了    

        
    # オープンリストの先頭の要素を返し、内容を更新するインスタンスメソッド
    def get_first(self):
        # 先頭の要素を削除しfirstに確保
        first = self.__openlist.pop(0)
        # openlistの先頭を削除したので、openlistの内容は更新済み
        # firstを返す
        return(first)
    # get_first　終了
    
    
    # オープンリストをコストとノードidでソートするインスタンスメソッド
    def sort_nodes(self):
        # operatorモジュールのmethodcaller関数を使って、
        # ノード(nid, pid, score)について予めnidでソートし、
        # その結果をscoreでソートする
        self.__openlist.sort(key=methodcaller("id"))
        self.__openlist.sort(key=methodcaller("f_hat"))
            

    # オープンリストにnode_listを追加するインスタンスメソッド（各自作成）
    def add_node_list(self, node_list, closed):
        # node_listとオープンリスト、クローズドリストから、
        # non_add: オープンリストに追加しないnode_listの要素のリスト
        # removed: オープンリストまたはクローズドリストから削除されるノードのリスト
        # をそれぞれ作成する
        non_add = []
        removed = []
        op_cl = self.__openlist + closed.elements()
        # non_addとremovedを作成する

                # op_clとnode_listで同じidのノードがある

                    # op_clに含まれるノードの方が評価値が大きいならば

                        # そのノードは削除の対象となる

                    else:
                        # node_listに含まれるノードの方が評価値が大きいので
                        # そのノードはオープンリストに追加されない


        # non_addに含まれるノードをnode_listから削除


        # removedに含まれるノードをオープンリストまたはクローズドリストから削除

        
        # オープンリストへの追加操作はnode_listにopenlistを結合することで実現


        # オープンリストをソートする
        self.sort_nodes()
    # add_node_list　終了
                        
        
# クローズドリストの定義
class ClosedList:
    # クローズドリストを空のリストで初期化
    def __init__(self):
        self.__closedlist = []
    # __init__　終了

    
    # クローズドリストの内容を返すインスタンスメソッド
    def elements(self):
        return(self.__closedlist)
    # elements　終了

    
    # クローズドリストに探索済みノードnodeを追加
    def add(self, node):
        self.__closedlist.append(node)
    # add　終了


    # クローズドリストから要素elmを除去するインスタンスメソッド
    def remove(self, elm):
        try:
            self.__closedlist.remove(elm)
        except ValueError:
            print(ValueError)
            return None
    
    # クローズドリストの内容を文字列で返すインスタンスメソッド
    def view(self):
        idx = 0
        cl = "["
        for node in self.__closedlist:
            if idx < len(self.__closedlist)-1:
                cl = cl + node.view() + ", "
                idx = idx + 1
            else:         
                cl = cl + node.view()
                idx = idx + 1
        cl = cl + "]"
        
        return(cl)
    # view　終了

# クローズドリストの定義　終了


# 状態空間の定義
class StateSpace:
    # 状態空間は有向グラフで表現する
    # 状態空間のノードは(節点id,ヒューリスティック評価値)で定義
    # 状態空間の辺は(始節点.id,終節点.id,コスト)で定義
    # 便宜上、id=0：ルートノード、id>=GOAL_THRESHOLD：ゴールノードとする
    
    def __init__(self):
        self.__node_set = [(ROOT_NODE,0),(1,7),(2,4),(3,6),(4,5),
                           (5,2),(6,3),(7,4),(8,2),(GOAL_THRESHOLD,0)]
        self.__edge_set = [(ROOT_NODE,1,1),(ROOT_NODE,2,3),(1,2,1),
                              (1,6,6),(2,3,6),(2,6,6),(2,7,3),
                              (3,4,5),(3,7,2),(3,8,4),
                              (4,8,2),(5,1,1),(6,5,7),(6,7,2),(7,8,1),
                              (7,GOAL_THRESHOLD,7),(8,GOAL_THRESHOLD,5)]
        # __init__　終了

    # ノードがidであるノードの次のノードとコストのリストを返す
    def next(self, id):
        next = []
        # idから到達できるノードidとそのg_hat,h_hatを求める
        for edge in self.__edge_set:
            if edge[0] == id:
                for nnode in self.__node_set:
                    if nnode[0] == edge[1]:
                        # 次のノードが持つコストを求める
                        nd = (nnode[0], edge[2], nnode[1])
                        next.append(nd)

        return(next)
    # next　終了
# 状態空間の定義終了
