#coding:UTF-8

# コストを考慮しない探索２
# 深さ優先探査億(depth_first_search)

import sys
import brute_force_search as bfs
import depth_first_search as dfs

# 探索の手順

# １．状態空間とオープンリスト、クローズドリストを初期化する
st = bfs.StateSpace()
openlist = dfs.OpenList()
closedlist = bfs.ClosedList()
step = 0

# オープンリストとクローズとリストの表示（各自作成）
print("openlist: " + openlist.view())
print("closedlist: " + closedlist.view() + "\n")

# ２．探索が失敗するか、ゴールノードを発見するまで探索を続ける
while (True):
    step += 1
    
    # ３．オープンリストが空である場合は探索失敗で終了する
    if openlist.is_empty():
        print("Depth First Search failed: Openlist is empty.")
        print("openlist: " + openlist.view())
        print("closedlist: " + closedlist.view() + "\n")
        sys.exit()

    # ４．オープンリストの先頭のノードを取得する
    else:
        current = openlist.get_first()


        # ５．先頭のノードがゴールノードであれば探索成功で終了する
        if current.is_goal():
            print("\n== SUCCEEDED!! ==\n")
            path = current.searched_path(closedlist)
            print("searched path: " + current.view_searched_path(path))
            print("step: " + str(step))
            print("openlist: " + openlist.view())
            print("closedlist: " + closedlist.view() + "\n")
            sys.exit()

        # ６．先頭のノードがゴールノードでない場合、次のノードを展開し
        # オープンリストの先頭に追加する
        else:
            next = current.expand(st)
            openlist.add_node_list(next, closedlist)


            # ７．先頭のノードは探索済みとしてクローズドリストに追加する
            closedlist.add(current)
            print("current: " + str(current.id()))
            print("openlist: " + openlist.view())
            print("closedlist: " + closedlist.view() + "\n")

            
        # 5.からのif_else終了
    # 3.からのif_else終了
    
# whileループ終了
