#coding:UTF-8

import pdb



# コストを考慮しない探索(Brute_force_search)
# 幅優先探索(Width_first_search)と深さ優先探索(Depth_first_search)での
# ノード、クローズドリスト、状態空間を本ファイルで定義する

# ルートノードのIDは0
ROOT_NODE = 0
# ルートノードの親ノード（存在しない）のIDは便宜上-1とする
ROOT_PARENT = -1
# 便宜上、ノードIDが1000以上のノードはゴールノードとみなす
GOAL_THRESHOLD = 1000

# ノード(Node)の定義
class Node:
    # ノード番号idと親ノード番号parentのノードを作成する
    def __init__(self, id, parent):
        self.__id = id
        self.__parent = parent
    # __init__終了

    
    # ノードのidを返すインスタンスメソッド
    def id(self):
        return(self.__id)
    # id　終了

    
    # ノードの親ノードのidを返すインスタンスメソッド
    def parent(self):
        return(self.__parent)
    # parent　終了

    
    # ノードの内容を返すインスタンスメソッド
    def elements(self):
        return((self.id(),self.parent()))
    # elements　終了

    
    # ノードの内容を文字列で返すインスタンスメソッド（各自作成）
    def view(self):
        return(str(self.id())+","+str(self.parent()))
    # view　終了

    
    # ノードがゴールノードかを判定するインスタンスメソッド（各自作成）
    def is_goal(self):
        # ゴールノードであるときはTrueを返す
        # ゴールノードでないときはFalseを返す
        return True if(self.id()>=GOAL_THRESHOLD) else False
    # is_goal 終了

    
    # 状態空間stを用いて、ノードから到達できる次のノードのリストを得る
    # インスタンスメソッド(各自作成)            
    def expand(self, st):
        # 次のノードのidのリストを初期化
        next = []
        # 次のノードを作成しnextに追加(各自作成)
        next_ids = st.next(self.id())
        for nid in next_ids:
            # ノードidがnid、親ノードidがself.id()のノードを作成
            nnode = Node(nid, self.id())
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
        cl.elements().reverse()

        return(sp)
    # searched_path　終了

    
    # 探索されたパスの内容を文字列で返すインスタンスメソッド
    def view_searched_path(self, sp):
        strsp = ""
        idx = 0
        for node in sp:
            if idx < len(sp)-1:
                strsp = strsp + node.view() + " -> "
                idx = idx + 1
            else:            
                strsp = strsp + node.view()
        return(strsp)        
    # view_searched_path　終了
# ノードの定義　終了


# クローズドリストの定義
class ClosedList:
    # クローズドリストを空のリストで初期化
    def __init__(self):
        self.__closed_list = []
    # __init__　終了

    
    # クローズドリストの内容を返すインスタンスメソッド
    def elements(self):
        return(self.__closed_list)
    # elements　終了

    
    # クローズドリストに探索済みノードnodeを追加
    def add(self, node):
        self.__closed_list.append(node)
    # add　終了

    
    # クローズドリストの内容を文字列で返すインスタンスメソッド(各自作成)
    def view(self):

        cl = "( "
        b = False

        for node in self.__closed_list:
            if b:
                cl += ", " + str(node.id())

            else:
                cl += str(node.id())
                b = True

        cl += " )"

        # クローズドリストの内容を表す文字列clを返す
        return(cl)
    # view　終了

# クローズドリストの定義　終了


# 状態空間の定義
class StateSpace:
    # 状態空間は有向グラフで表現する
    # 状態空間は(始節点.id,終節点.id)で表す辺のリストで定義
    # 便宜上、id=0：ルートノード、id>=GOAL_THRESHOLD：ゴールノードとする
    
    def __init__(self):
        self.__state_space = [(ROOT_NODE,1),(ROOT_NODE,2),(1,2),(1,6),
                              (2,3),(2,6),(2,7),(3,4),(3,7),(3,8),
                              (4,8),(5,1),(6,5),(6,7),(7,8),
                              (7,GOAL_THRESHOLD),(8,GOAL_THRESHOLD)]
    # __init__　終了

    # ノードidの次のノードidのリストを返す
    def next(self, id):
        next = []
        # idから到達できるノードidを取得する（各自作成）
        for e in self.__state_space:
          if e[0] == id:
            next.append(e[1])
                
        return(next)
    # next　終了
# 状態空間の定義終了
