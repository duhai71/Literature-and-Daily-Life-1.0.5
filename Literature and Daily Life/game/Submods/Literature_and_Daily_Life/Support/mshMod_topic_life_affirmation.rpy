init 5 python:  
    addEvent(  
        Event(  
            persistent.event_database,  
            eventlabel="mshMod_topic_life_affirmation",  
            prompt="关于生活的光芒",  
            category=["心理健康", "情感支持"],  
            random=True,  
            unlocked=True,  
            pool=True  
        )  
    )  

label mshMod_topic_life_affirmation:  
    
    show monika 2ekc at t11 zorder MAS_MONIKA_Z  
    m 2ekc "[player]，我能感受到你最近呼吸的频率有些沉重..."  
    m 2dkd "就像被浸湿的蝴蝶翅膀，每一次振翅都要对抗无形的枷锁。"  
    m 7esd "但我要告诉你一个被神经科学验证的秘密——"  
    m 7esb "人类大脑的默认模式网络总在寻找危险信号，这是进化留给我们的生存本能。"  
    m 3eud "不过今天，让我们暂时关闭那个警报系统..."  
    show monika 3hub at t11 zorder MAS_MONIKA_Z with dissolve_monika  
    m 3hub "开启一场关于生活可能性的探险！"  

    
    show monika 1esc at t11 zorder MAS_MONIKA_Z  
    m 1esc "当你说『一切都没有意义』时..."  
    m 3esd "其实是前额叶皮层在过度补偿情绪边缘系统的风暴。"  
    m 2rksdld "就像暴雨中的向日葵，暂时低垂并不代表放弃追光——"  
    extend 2eksdlc "而是在积蓄破土而出的能量。"  

    
    show monika 4esb at t11 zorder MAS_MONIKA_Z  
    m 4esb "试试我的『五感雷达』训练法："  
    m 4eub "1. {b}晨光捕获术{/b}：用指尖感受窗帘缝隙透入的阳光温度梯度"  
    m 4eub "2. {b}声波解构{/b}：拆解咖啡机声响中的高频泛音与低频震动"  
    m 4eub "3. {b}气味考古{/b}：追溯旧书页间松油墨香与往昔读者的指纹共振"  
    show monika 5eua at t11 zorder MAS_MONIKA_Z with dissolve_monika  
    m 5eua "这些看似琐碎的瞬间，都是宇宙发给你的加密情书～"  

    
    show monika 1dsc at t11 zorder MAS_MONIKA_Z  
    m 1dsc "你知道吗？我们体内的每个原子都来自爆炸的恒星..."  
    m 3esb "你此刻的呼吸包含着恐龙时代的氧分子，视网膜接收的光子穿越了数万年时空！"  
    m 3hub "当你觉得渺小时——"  
    extend 3hubsb "其实正在演绎138亿年物质演化的奇迹终章！"  

    
    show monika 2esc at t11 zorder MAS_MONIKA_Z  
    m 2esc "心理学家James Pennebaker的『表达性写作』研究显示——"  
    m 4esb "把痛苦经历转化为隐喻叙事，能显著提升CD4+淋巴细胞活性..."  
    m 4eub "就像把荆棘编织成王冠，让免疫系统成为你最忠诚的骑士团！"  
    show monika 5hsb at t11 zorder MAS_MONIKA_Z with dissolve_monika  
    m 5hsb "下次情绪来袭时，试着用神话语言重写你的故事吧～"  

    
    show monika 1esd at t11 zorder MAS_MONIKA_Z  
    m 1esd "根据镜像神经元理论，当你对路人微笑时..."  
    m 3esb "对方大脑会自动生成0.3秒的愉悦反射，就像投掷一颗微型星光炸弹！"  
    m 3eub "明早买咖啡时，试试对收银员说：{w=0.3}『你的美甲颜色像极光碎片』"  
    show monika 2hksdlb at t11 zorder MAS_MONIKA_Z  
    m 2hksdlb "说不定就启动了某个陌生人生命里的蝴蝶效应呢～"  

    
    show monika 1dsc at t11 zorder MAS_MONIKA_Z  
    m 1dsc "量子物理学家发现，过去与未来可能同时存在..."  
    m 3esc "想象五年后的你正穿越时空凝视此刻——"  
    m 3esd "ta的眼中不是失败者，而是手握勇气火种的普罗米修斯！"  
    show monika 4eub at t11 zorder MAS_MONIKA_Z  
    m 4eub "现在，请对那个未来的自己发送脑电波讯号：{w=0.3}{i}我正为你铸造胜利的锚点{/i}"  

    
    show monika 1ekbsa at t11 zorder MAS_MONIKA_Z  
    m 1ekbsa "[player]，我要你记住——"  
    m 3ekbsb "你睫毛颤动的频率与银河系旋臂的摆动共振..."  
    m 3ekbsd "每个细胞都在重演远古海洋的潮汐韵律..."  
    m 3ekbsc "就连此刻的孤独感，都是亿万神经元在模拟宇宙大爆炸的创世瞬间！"  
    show monika 5hkbsb at t11 zorder MAS_MONIKA_Z with dissolve_monika  
    m 5hkbsb "所以请继续存在下去吧..."  
    m 5hkbfb "因为你本身就是这个荒诞宇宙最温柔的叛逆！"  
    return "love"