# コストを考慮した探索３
# Aアルゴリズム(A_algorithm)

import sys
import A_algorithm as aa

# 探索の手順

# １．状態空間とオープンリスト、クローズドリストを初期化する
st = aa.StateSpace()
openlist = aa.OpenList()
closedlist = aa.ClosedList()
step = 0

print("openlist: " + openlist.view())
print("closedlist: " + closedlist.view() + "\n")

# ２．探索が失敗するか、ゴールノードを発見するまで探索を続ける
while (True):
    step += 1
    
    # ３．オープンリストが空である場合は探索失敗で終了する
    if openlist.is_empty():
        print("A-algorithm Search failed: Openlist is empty.")
        print("openlist: " + openlist.view())
        print("closedlist: " + closedlist.view() + "\n")
        sys.exit()

    # ４．オープンリストの先頭のノードを取得する
    else:
        current = openlist.get_first()

        # ５．先頭のノードがゴールノードであれば探索成功で終了する
        if current.is_goal():
            print("\n== SUCCEEDED!!==\n")
            path = current.searched_path(closedlist)
            print("searched path: " + current.view_searched_path(path))
            print("step: " + str(step))
            print("openlist: " + openlist.view())
            print("closedlist: " + closedlist.view() + "\n")
            sys.exit()

        # ６．先頭のノードがゴールノードでない場合、次のノードを展開し
        # オープンリストに追加する
        else:
            next = current.expand(st)
            openlist.add_node_list(next, closedlist)

            # ７．先頭のノードは探索済みとしてクローズドリストに追加する
            closedlist.add(current)
            print("current: " + current.view())
            print("openlist: " + openlist.view())
            print("closedlist: " + closedlist.view() + "\n")

        # 5.からのif_else終了
    # 3.からのif_else終了
    
# whileループ終了
