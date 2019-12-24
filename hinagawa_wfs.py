#coding:UTF-8

# コストを考慮しない探索１
# 幅優先探査億(width_first_search)

import sys
import brute_force_search as bfs
import width_first_search as wfs

# 探索の手順

# １．状態空間とオープンリスト、クローズドリストを初期化する
st = bfs.StateSpace()
openlist = wfs.OpenList()
closedlist = bfs.ClosedList()
step = 0
# オープンリストとクローズとリストの表示（各自作成）

# ２．探索が失敗するか、ゴールノードを発見するまで探索を続ける
while (True):
    
    # ３．オープンリストが空である場合は探索失敗で終了する
    # プログラムの実行はsys.exit()で行う

    
    # ４．オープンリストの先頭のノードを取得する
    else:


        # ５．先頭のノードがゴールノードであれば探索成功で終了する

            sys.exit()
        # ６．先頭のノードがゴールノードでない場合、次のノードを展開し
        # オープンリストの末尾に追加する
        else:

            # ７．先頭のノードは探索済みとしてクローズドリストに追加する

            
        # 5.からのif_else終了
    # 3.からのif_else終了
    
# whileループ終了