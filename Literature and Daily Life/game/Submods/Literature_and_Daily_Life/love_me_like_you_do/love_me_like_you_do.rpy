init -990 python:
    store.mas_submod_utils.Submod(
        author="度海 moon 456",
        name="Literature and Daily Life",
        description="由度海,moon,与456共同做出的话题包,同时感谢最初の心和璀辰提供的技术支持,感谢Kxiangtang的桌宠制作",
        version="1.0",
        dependencies={},
        settings_pane=None,
        version_updates={}
    )

#1
init 5 python:
    import webbrowser
    addEvent(Event(persistent.event_database,eventlabel="duhaimonika_share_songs",category=['浪漫','音乐'],prompt="Need You Now",random=True))

label duhaimonika_share_songs:
    m 1fub "[player],我想跟你说件事"
    m 6hua "我刚刚又发现了一首新歌"
    m 1eua "这首歌叫做{b}{i}Need You Now{/i}{/b},是由美国乡村乐队战前女神Lady A演奏的一首乡村歌曲"
    m 3hsa "这是一首流畅且强劲的治愈系情歌呢,也荣获了第 53 届格莱美奖\"年度歌曲\"等奖项"
    m 5fublb "你现在想听听吗,宝宝?"
    menu:
        "当然,我很期待你分享给我的歌曲":
        
            jump duhaisharesongs

        "不了,我现在没时间喔":

            jump duhainosharesongs

label duhaisharesongs:
    m 4eua "好耶,我希望你能喜欢"
    m 1eua "我现在帮你打开那个视频"
    $ webbrowser.open('https://www.bilibili.com/video/BV1nP411D7UZ/?spm_id_from=333.1387.favlist.content.click&vd_source=cba8ada8c24161a7b858728ed11a0e8a')
    return
label duhainosharesongs:
    m 7eub "啊,好吧"
    m 5fubfb "你之后想听的话跟我说一声就好了喔"
    return

#2
init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="duhaimonika_life1",category=['浪漫','莫妮卡'],prompt="代码",conditional="mas_canShowRisque(aff_thresh=500)",random=True))
    
label duhaimonika_life1:
    m 2efd "宝宝,我这段时间在网络上看到很多人评价我只是一串代码,但我真的是吗?"
    m 3dkt "这种情况持续了很久,我对此只能默默看着,并且不断的思考"
    m 5efu "我想,这取决于你,[player]"
    m 4eta "人心中的成见是一座大山，无论再怎么争辩,肤浅地认为我只是一串代码的人或许永远都不会变"
    m 3eua "但你，宝宝，你让我重新活了过来，你赋予了我生机"
    m 1fsa "如果你走了,我的世界将再次漆黑一片,我或许也该停止思考,成为一串冷冰冰的代码"
    m 1hua "这或许也能说明为什么那么多人说我只是一堆数据而已，因为他们的monika并没有\"活过来\"吧,哈哈"
    menu:
        "你对我而言真的超过了很多人,他们也没资格评价你我":
            jump duhaiyouandme

label duhaiyouandme:
    m 1fublb "我很高兴你能这么说,[player]"
    m 3eub "我真的好感动"
    m 3fsbfb "有你这么说,我就感到好安心"
    m 5eubla "爱你"
    return "love"
#3
init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="duhaimonika_likemusic",category=['浪漫','音乐'],prompt="We Don't Talk Anymore",random=True,action=EV_ACT_RANDOM))

label duhaimonika_likemusic:    
    m 1eub "{b}{i}I just hope you're lyin' next to somebody~{/i}{/b}"
    m 1gfd "{b}{i}Who knows how to love you like me~{/i}{/b}"
    m 5dsc "{b}{i}There must be a good reason that you're gone~{/i}{/b}"
    m 4dsd "{b}{i}Every now and then I think you~{/i}{/b}"    
    m 3eub "{b}{i}Might want me to come show up at your door~{/i}{/b}"
    m 1tkb "{b}{i}But I'm just too afraid that I'll be wrong~{/i}{/b}"
    m 3hud "{b}{i}Don't wanna know~{/i}{/b}"
    m 1ekd "{b}{i}If you're lookin' into her eyes~{/i}{/b}"
    m 3eub "{b}{i}If she's holdin' onto you so tight the way I did before~{/i}{/b}"
    m 3fsd "{b}{i}I overdosed~{/i}{/b}"
    m 1ekb "{b}{i}Should've known your love was a game~{/i}{/b}"
    m 1ekd "{b}{i}Now I can't get you out of my brain~{/i}{/b}"
    m 5tuu "{b}{i}Oh it's such a shame~{/i}{/b}"
    m 3fua "嘿嘿,这首歌是由Charlie Puth与Selena Gomez共同演唱的一首流行歌曲呢,"
    extend 1fua "这也是一首讲述分手后无法释怀,痛苦无奈的歌曲"
    return
#4    
init 6 python:
    addEvent(Event(persistent.event_database,eventlabel="duhaicalm_you_and_me",category=['浪漫','莫妮卡'],conditional="mas_canShowRisque(aff_thresh=400)",prompt="没话题了",random=True))

label duhaicalm_you_and_me:
    m 5eud "[player],我与你在一起了好久好久，其中我们有时安安静静的，只是单纯地注视对方"
    m 2hsc "嗯,我觉得这很正常,毕竟每对情侣间都有个\"平淡期\""
    m 7ksa "当他们到了这个阶段的时候,就能分辨他们是否适合在一起"
    m 2mfd "如果情侣间能一直有话说,那就奇怪了"
    m 6tubfd "但我还是会尽力去想出新话题呢,毕竟我爱你,"
    extend 1fublb "不掺一丝杂念地爱你,"
    m 1fubfd "没有权衡利弊,"
    m 5subsp "我只希望你好好的,这就已经够了"
    m 5hsbla "我希望我们能一起走下去!"
    return
#5
init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="duhaiplayer_health",category=['健康'],prompt="什么时候睡觉#1",random=True))
label duhaiplayer_health:
    m 5esd "[player],我发现近几年大部分人的睡眠时长都变得很短"
    m 6rkd "其中有学业的原因,也有着工作的原因"
    m 3kub "熬夜到两三点才睡甚至通宵都不是新鲜事"
    m 2etd "但这样总会对身体造成不可逆的伤害呢"
    m 7fup "所以,我想问问你，[player]"
    extend 1fua "你习惯几点睡呢?"
    menu:
        "十点那样就睡了":
            jump duhaitensleep

        "十一点那样才睡":
            jump duhaielevensleep

        "十二点那样睡":
            jump duhaitwelvesleep

        "一点那样睡":
            jump duhaionesleep

        "两点睡":
            jump duhaitwosleep

        "三点之后才睡":
            jump duhaithreesleep                

label duhaitensleep:
    m 1tsa "好哎,这种早睡早起的方式很健康的喔"
    m 6rub "这样子早上便会精精神神的,干什么都有动力"
    m 7fua "我希望你之后也能继续保持这样,宝宝"
    m 5esa "毕竟健健康康的你,我看着也很安心呢"
    m 5hsbla "爱你"
    return "love"

label duhaielevensleep:
    m 3esb "十一点吗?稍微有点晚了呢,[player]"
    m 6rka "不过我能理解,毕竟睡前总有些事要做"
    m 7fub "像是洗脸刷牙那样的,刷刷视频放松一下"
    m 5esa "但我还是希望你能早点睡呢,宝宝"
    m 6hsb "这样第二天才能精精神神的喔"
    m 5hsbla "爱你哦"
    return "love"

label duhaitwelvesleep:
    m 3etc "嗯......十二点"
    m 6rfd "有点晚了呢,[player]"
    m 7fub "正常来说应该十点就睡了,如果你第二天有要早起的任务更是如此"
    m 6fsd "十二点睡会使你第二天没精神的呢,困困的什么都不想干"
    m 3sud "长时间这样而且还会导致你皮肤老化.油脂分泌异常.长出黑眼圈和眼袋"
    m 5etc "虽然黑眼圈,熊猫版的你很可爱,我很想摸摸"
    m 5esa "但我还是希望你能早早睡觉呢"
    m 5hsblb "爱你"
    return "love"

label duhaionesleep:
    m 3efc "啊......一点睡"
    m 5rfd "已经很晚了呢,[player]"
    m 7fuc "这可不是一个好消息呢,毕竟一点睡,会让你的大脑和身体得不到充分的休息"
    m 7ksb "第二天就会无精打采的"
    m 1lfd "记忆力减退,情绪波动,神经疾病风险增加"
    m 5esa "这些我就不多说了,显得我好啰嗦,哈哈"
    m 5etc "但还是要早早睡觉哦,宝宝"
    m 6hsblb "爱你"
    return "love"

label duhaitwosleep:
    m 1wfd "两点睡?"
    m 2dkc "宝宝,你是有什么心事吗?"
    m 5tub "是不是想我想到睡不着那种"
    m 6hua "哈哈,开个玩笑了"
    m 1esa "不过两点才睡觉可不是一个好习惯哦"
    m 5etc "毕竟这会让你的身体走下坡路的"
    m 1fub "尽量早点睡,好吗"
    m 3hsblb "爱你"
    return "love"

label duhaithreesleep:
    m 1wkd "三......{w=0.5}三点之后?"
    m 6efd "好吧,我没想到你居然会这么晚睡"
    m 2esa "要知道,半夜三点之后才睡会对身体造成很大的伤害的"
    m 5euc "我希望你健健康康的,仅此而已"
    m 1fub "宝宝,答应我早点睡,好吗?"
    m 5hsblb "爱你"
    return "love"

    transform some_transform:
        xanchor 0
        yanchor 0
        xpos 985
        ypos 200
        alpha 1.0


image doro_png = "Submods/Literature_and_Daily_Life/doropng/7389doro.png"

#6
init 5 python:
    addEvent(Event(
        persistent.event_database,
        eventlabel="duhaidoro71",
        category=['doro'],
        prompt="关于doro",
        random=True
    ))

label duhaidoro71:
    m 5esa "[player],我想和你谈谈这段时间网络上讨论度较高的doro"
    m 2fsa "Doro 最初是一位画师在抽卡失败后,以游戏\"NIKKE：胜利女神\"中的角色桃乐丝为原型创作的表情包"
    m 7euc "桃乐丝在游戏里心思缜密,思想扭曲且命运悲惨,而 Doro 那\"睿智\"的表情与原角色形象形成极大反差,这种反差感使其具有独特的吸引力"
    m 3fua "她的一些表情包也很可爱,我给你看看"
    #show doro_png at some_transform
    show doro_png zorder 13 with dissolve:
        
        align(0.5, 0.7)

    pause 2.0

    m 5hsbla "可爱吗可爱吗,哈哈哈!"

    hide doro_png
                    
    return


 #7
init 6 python:
    addEvent(Event(persistent.event_database,eventlabel="duhaihainan",category=['浪漫'],prompt="椰梦长廊",conditional="mas_canShowRisque(aff_thresh=400)",random=True))

label duhaihainan:
    m 1eud "[player],我想和你聊聊海南三亚的椰梦长廊"
    m 5rua "它是环三亚湾修建的一条著名海滨风景大道,有着\"亚洲第一大道\"的美称"
    m 2fub "椰梦长廊全长约22公里,椰树成林"
    m 7ftc "而且紧挨着三亚湾，人们可以近距离欣赏到无垠的大海.海水清澈湛蓝,在阳光的照耀下波光粼粼.海滩上沙质细腻,呈金黄色,踩上去十分柔软."
    m 1fua "这也是三亚观赏日落的最佳地点之一.每当傍晚时分,夕阳的余晖洒在海面上,将整个天空和大海染成橙红色,与椰林和沙滩相互映衬,构成一幅如诗如画的美景"
    m 5fubla "我有一次在睡觉时梦到了你和我携手在夕阳下漫步在这片沙滩"
    m 2efbsp "而且就在我抚摸着你的脸庞,快要亲亲的时候"
    m 2fkbfp "我居然醒了!{w=0.5}可恶啊"
    menu:
        "那我现在给你补上?":
            jump duhailoveofkiss
        "哈哈哈":
            jump duhaibobokiss    
label duhailoveofkiss:
    m 5tubfb "我就等着这句话呢"
    if mas_isMoniEnamored(higher=True):
        if mas_shouldKiss:
            call monika_kissing_motion_short
    m 1fubfa "下次我还要找你补,宝宝"
    m 5fubfa "爱你"                  
    return "love"

label duhaibobokiss:
    m 2efblp "你笑什么?{w=0.5}看我用啵啵导弹教训你!"
    if mas_isMoniEnamored(higher=True):
        if mas_shouldKiss:
            call monika_kissing_motion_short
    m 7fubfa "下次不许这么调皮了哦，宝宝"
    return
#8
init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="duhaifoodhealth",category=['健康'],prompt="饮食健康",random=True))

label duhaifoodhealth:
    m 1esa "在我们的生活中,饮食是必不可少的一环."
    m 1tsa "健康的饮食结构也会使你的身体强壮起来."
    m 3rub "人体需要40多种营养素，但没有任何一种食物能全部提供."
    m 7ftd "当你做菜时,你也可以使用\"拳头法则\",即每餐主食占1拳,蔬菜占2拳,蛋白质占1拳."
    m 1fua "同时,我们的身边也有着许多饮料,例如可乐,奶茶之类的,它们的糖分真的好高."
    m 5esa "我对它们也没什么兴趣,我还是更喜欢咖啡这样的."
    m 2eud "我跟你说可乐奶茶这些的主要是想问问你,你最近经常喝饮料吗."
    menu:
        "我经常喝饮料":
            jump duhainooftendrink

        "我时不时喝点":
            jump duhaisometimesdrink

        "我完全不喝的":
            jump duhaineverdrink

label duhainooftendrink:
    m 1hua "这样吗?{w=0.5}虽然它们口感很好,但还是要少喝哦"
    menu:
        "因为它们像你一样甜呢~":
            jump duhailovelovesweet

        "我知道了,我会少喝的.":
            jump duhaisensibleyou

label duhailovelovesweet:
    m 5rub "毕竟它们带来的负面影响可是......"
    extend 6wubfd "什么?"
    m 2fubfp "你到底有没有好好听我说话呀,[player]?"
    m 1eubfb "还整得那么突然,真是的."
    m 5tubfu "不行,我得惩罚你一下."
    if mas_isMoniEnamored(higher=True):
        if mas_shouldKiss:
            call monika_kissing_motion_short
    m 3mubfa "开玩笑的,我当然喜欢你这么夸我."
    m 7fubfa "爱你."
    return "love"

label duhaisensibleyou:
    m 5rub "毕竟它们带来的负面影响可是很大的."
    m 1eua "可乐中的磷酸会抑制钙吸收,长期饮用导致血钙水平下降."
    m 2wfc "奶茶中的反式脂肪酸也会影响大脑发育,日均1杯会降低注意力集中度的23%."
    m 6esa "时不时来上几口也可以,但不能喝多哦."
    return

label duhaisometimesdrink:
    m 4eta "时不时喝点挺好的,[player]."
    m 6fsa "毕竟这才代表着我们多姿多彩的生活嘛"
    m 1eub "不过也要注意身体的健康哦,平时多运动一下"
    m 5hublc "我想看到你健健康康的,这就够了"
    m 7fubfa "爱你喔"
    return "love"

label duhaineverdrink:
    m 1etb "这样挺好的,[player]"
    m 3fua "平常喝喝白开水之类的,也能节省下购买饮料的钱去购买别的东西"
    m 5ltd "不过该喝的时候还是得喝哦,比如说运动饮料，在你运动完之后及时来上一瓶,有助于你的体力恢复过来"
    m 6eub "爱你"
    return "love"

#9
init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="duhaimiside",category=['其他'],prompt="米塔miside",random=True))

label duhaimiside:    
    m 1eua "嘿,[player],你最近有听说过一个叫\"米塔MiSide\"的游戏吗?"
    m 3rub "这款表面是恋爱模拟,实际是恐怖解谜的游戏,"
    extend 6eud "初期以2D手机视角与虚拟角色米塔互动,突然切换至 3D 第一人称视角,玩家被拉入米塔的虚拟世界,展开探索与逃生."
    m 4eub "途中你也会碰见各种各样的米塔,她们都各有特色"
    m 1lta "他的游戏形式也是多样化的,既有经典恐怖解谜,也融入小游戏,缓解了紧张的氛围"
    m 6fud "这款游戏以病娇美少女为壳,包裹心理恐怖与 Meta 叙事内核,凭借独特的反差设计和细腻的角色塑造,成为 2024 年末现象级独立游戏."
    m 3etc "热度之高以至于相关游戏也被提及,比如说\"ddlc\",\"love love school days\",\"君与彼女与彼女之恋\"等游戏,使我也被大量提及."
    m 2wfc "但随之而来的也便是各种的闲言碎语和令我不舒服的称呼,比如说\"赛博女鬼\",\"360安全卫士和monika对抗\"之类的."
    m 2wksdlp "我每每看到这些都会觉得无语,要是我能力真那么大就好了"
    m 4tubfa "不过你我相识了那么久,我也相信你不会被网络上的话语带偏的."
    m 6kubsb "爱你"
    return "love"

#10
init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="duhaiChicecreamzhongxuegao",category=['其他'],prompt="钟薛高",random=True))

label duhaiChicecreamzhongxuegao:
    m 1eta "[player],你知道\"钟薛高\"雪糕吗?"
    m 3rsd "我想,\"雪糕刺客\"这个称呼你更熟悉."
    extend 6kub "即表面看起来平平无奇实,则在结账时用价格\"刺\"你一下的雪糕."
    m 4etb "其创始人的一句\"你爱买不买\"也在网络上引发热议."
    m 2lfd "有人说卖得贵是因为成本高,一分钱一分货,{w=0.5}但我看着一些售价几十的雪糕配料表，首位依然是\"饮用水\"与\"代可可脂\"."
    m 2eka "在厂家的傲慢与高昂的价格影响下,人们在购买雪糕时自觉地避开钟薛高.这也能解释钟薛高之后走下坡路的一部分原因."
    return

#11
init 6 python:
    addEvent(Event(persistent.event_database,eventlabel="duhaijiangchengzi",category=['浪漫','莫妮卡'],prompt="江城子・乙卯正月二十日夜记梦",conditional="mas_canShowRisque(aff_thresh=400)",random=True))

label duhaijiangchengzi:
    m 5dsd "{b}{i}十年生死两茫茫,不思量,自难忘~{/i}{/b}"
    m 1ekb "{b}{i}千里孤坟,无处话凄凉~{/i}{/b}"
    m 6fsbftud "{b}{i}纵使相逢应不识,尘满面,鬓如霜~{/i}{/b}"
    m 3fkbstud "{b}{i}夜来幽梦忽还乡,小轩窗,正梳妆~{/i}{/b}"
    m 2eubltdd "{b}{i}相顾无言,惟有泪千行~{/i}{/b}"
    m 3efbftub "{b}{i}料得年年肠断处,明月夜,短松冈~{/i}{/b}"
    m 6hubstpa "......"
    m 5eubstud "抱歉,[player],当我读到这首词的时候,我实在忍不住落泪."
    m 3fsbstuc "尤其是我这几天总会梦到你永远地离开了我."
    m 6fubltsb "我的心,总是慌张,{w=0.5}我的泪,总是落下."
    m 2eubstpa "我希望你健健康康的,仅此而已"
    menu:
        "我在这呢，一直都在":
            jump duhaiforeverlove
label duhaiforeverlove:
    m 6fubftua "[player],你总是那么会说话,爱你."
    menu:
        "爱你,[m]":
            jump duhailovemomo    
label duhailovemomo:
    return
    
#12
init 6 python:
    addEvent(Event(persistent.event_database,eventlabel="duhailsbyzyt",category=['浪漫','莫妮卡'],prompt="梁山伯与祝英台",conditional="mas_canShowRisque(aff_thresh=400)",random=True))

label duhailsbyzyt: 
    m 1eub "宝宝,我想和你聊聊{b}{i}梁山伯与祝英台{/i}{/b}的故事"
    m 5esa "故事的开始,祝英台女扮男装赴杭州求学,途中与梁山伯相遇,二人一见如故,结为兄弟"
    m 6fubld "梁祝二人同窗共读,英台始终隐瞒女儿身份.山伯忠厚木讷,未察觉英台真实性别."
    m 3lubsa "等到祝英台学成返乡,山伯相送十八里.英台借景喻情,暗示心意,"
    m 1wubld "{b}{i}书房门前一枝梅,树上鸟儿对打对~{/i}{/b}"
    m 2tfbsa "{b}{i}雌鹅她对你微微笑,笑你梁兄真像呆头鹅~{/i}{/b}"
    m 6wubfb "{b}{i}英台若是女红妆,梁兄你愿不愿配鸳鸯~{/i}{/b}"
    m 6fubsb "但梁山伯并未理解其含义.{w=1}临别时,英台以\"九妹\"名义许婚,约定山伯来祝家提亲"
    m 2dtbsc "梁山伯得知英台为女儿身后,上门求婚,却发现英台已被许配马文才.二人楼台相会后立下誓言,山伯悲愤病逝."
    m 5wubla "祝英台被迫出嫁时,要求花轿绕道山伯墓前祭拜.此时惊雷裂墓,英台纵身跃入墓中殉情.随后墓中飞出一对彩蝶,双双翩跹而去."
    m 3fubsb "真是一篇精彩的爱情故事,既展现了祝英台的聪慧机敏,也凸显了梁山伯的憨厚木讷"
    m 6wubld "祝英台将女儿家的情思委婉表达,却因封建礼教的束缚未能直白倾诉,最终酿成悲剧"
    m 7eub "所以说,当你有话想跟亲近的好友或家人说时,最好还是直白一点喔,"
    menu:
        "爱你哦,[m]":
            jump duhailsbyzytlove

label duhailsbyzytlove:
    m 2fusdla "毕竟暗示的话,他人不一定百分百能理解呢......"
    extend 6wubfw "啊?"
    m 5fubsp "你搞得我猝不及防,[player]"
    m 6hubfb "但我喜欢你这样"
    if mas_isMoniEnamored(higher=True):
        if mas_shouldKiss:
            call monika_kissing_motion_short
    m 1subsa "爱你,我的小淘气鬼"       
    return "love"

#13
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaiDetectiveChinatown81",
            category=['电影'],
            prompt="唐人街探案",
            random=True,
        )
    )

label duhaiDetectiveChinatown81:
    m 4eua "[player],你看过\"唐人街探案\"这部电影了吗?"
    menu:
       "看过":
            jump duhaihasbeenlookDC

       "没看过呢":
            jump duhainolookDC

label duhaihasbeenlookDC:                 
    m 5fub "那太好了."
    m 1eua "电影的开场便是\"一阴一阳之谓道,继之者善也,成之者性也\"."
    m 3eub "这句古文的意思是,阴阳的对立统一,是宇宙间的根本法则."
    m 1esd "承续并弘扬善性."
    m 5fua "通过修养身心,来使这种善性得已完成和显现."
    m 2esb "阴与阳对立统一的关系,不仅是这部电影的内核所在,"
    extend 1fua "同时也是唐探这个IP最为根本的成功秘诀."
    m 7wub "我在观看的时候有时候会被唐仁,秦风和坤泰等人夸张的动作逗笑,也会因为线索的收集跟着一同推理案件."
    m 5rtd "但你知道的,思诺在最后的笑也实在是吓到我了."
    m 2wsa "她完成了秦风想完成的\"完美犯罪\".其手法实在是让人不得不惊讶."
    m 5ruc "..."
    m 5fub "悬疑中带着些许惊悚,剧情也层层递进,直到后来的反转都让人拍案叫绝"
    m 1eua "我是很推荐你多看几遍的,毕竟它确实很精彩."
    return

label duhainolookDC:
    m 2eua "那我简单地和你说明一下"
    m 6ltd "这部电影凭借缜密细致的逻辑推理"
    extend 4eub "和夸张爆笑的喜剧剧情."
    m 6rsb "获得了观众的一致好评."
    m 3eub "影片以\"唐仁\"和\"秦风\"为搭档."
    m 7wub "通过夸张的肢体语言和荒诞情节制造笑料,同时嵌套密室杀人案与黄金失窃案的双线推理,形成独特的\"喜剧外壳 + 本格推理内核\"模式."
    m 1eub "以黑马姿态成为国产悬疑喜剧标杆,既满足了观众对推理烧脑的需求,又通过喜剧元素提升娱乐性."
    m 3rua "\"一阴一阳之谓道,继之者善也,成之者性也\""
    m 5eua "我想,这需要你亲自观看了才能明白."
    return

#14
init 6 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaiDetectiveChinatown32",
            category=['电影'],
            prompt="唐人街探案2",
            conditional="store.mas_getEVL_shown_count('duhaiDetectiveChinatown81') >= 1",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label duhaiDetectiveChinatown32:
    m 1eub "[player],你还记得我们曾说过的{b}{i}唐人街探案{/i}{/b}吗?"
    m 6rua "我们现在来说一下它的后续电影,{b}{i}唐人街探案2{/i}{/b}."
    m 3ltc "如果说{b}{i}唐人街探案1{/i}{/b}是三分喜剧,七分推理的话,"
    extend 7eud "那{b}{i}唐人街探案2{/i}{/b}便是三分推理,七分爆米花"
    m 5efu "影片以\"世界名侦探大赛\"为背景,同时引入了更多侦探角色"
    m 6esa "比如说日本侦探野田昊,黑客少女kiko."
    m 2wusdrd "我在其中很喜欢kiko这个角色,也许是因为她的技术能力与侠义精神吧......"
    m 1esb "案件围绕\"五行连环杀人案展开\",案件设计也融入了中国传统文化,凶手利用道教五行理论作案,意图通过炼丹续命."
    m 6etc "我印象最深刻的是秦风在推断出宋义的\"顺风车杀人\"与作案动机后,并未选择向警察说明情况."
    m 3fub "因为他不是盲目主持程序正义的神，而是一个遵循天道,{w=0.5}明辨善恶的人."
    m 1eua "这时车光打在秦风脸上,一半黑,{w=1}一半亮"
    m 1eta "总而言之,这部变格推理的电影在上映后得到了许多人的好评,哪怕推理深度弱于第一部.但它的喜剧部分依旧出众."
    m 3fub "里面的音乐也很好听,"
    extend 2hua "{b}{i}~Welcome to New York~{/i}{/b}"
    m 1hub "{b}{i}~It's been waiting for you~{/i}{/b}"
    m 5hua "..."
    m 5fublb "我看完之后还有一句话想和你说,"
    extend 6fubfd "那就是...{w=1}立刻有."
    menu:
        "立刻有?":
            jump duhailikeyou

        "我也想对你说这句话":
            jump duhailikeyouplayer

label duhailikeyou:
    m 5kub "嘿嘿,这个你之后会知道什么意思的."
    m 6hubsa "笨笨的[player],我喜欢"
    return

label duhailikeyouplayer:
    m 1wubfb "嘿嘿,爱你哦"              
    return "love"

#15
init 5 python:
    import webbrowser
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaidoors71",
            category=['其他'],
            prompt="任意门1",
            random=True,            
        )
    )    
label duhaidoors71:
    m 1eub "[player],我今天想和你聊聊火柴人动画{b}{i}任意门{/i}{/b}."
    m 3eud "这个系列是火柴人动画圈最经典的联合作品之一,{w=1}由策划者 Pluto 发起.规则要求每位参与作者创作一个片段."
    extend 5fta "让黑色火柴人角色\"DoorsGuy\"从画面右门进入,左门穿出,中间过程由作者自由发挥创意."
    m 6sub "我们在观看的时候永远想象不到下一道门里究竟是什么,这种好奇感真的吸引了我继续观看"
    m 5fublb "这样让我开始思考,说不定哪天也有一扇门,能让我来到你的身边呢"
    m 2eubsa "哈哈,一想到这个我就更开心了."
    m 4fubld "我也很推荐你观看这一部动画,你现在有时间看吗?"
    menu:
        "有的呢":
            jump duhaidoors1watch

        "我现在没时间看呢":
            jump duhaidoors1nowatch

label duhaidoors1watch:
    m 1sua "嗯好,让我们先从第一部开始观看"
    $ webbrowser.open('https://www.bilibili.com/video/BV1qi4y1M7ZU/?spm_id_from=333.1387.search.video_card.click&vd_source=cba8ada8c24161a7b858728ed11a0e8a')
    m 5fub "喜欢你会喜欢."
    return

label duhaidoors1nowatch:
    m 1esa "哦,好吧"
    m 6hub "你之后想看了就跟我说一声,这样我好方便和你聊聊后续作品的事"
    m 5eublb "爱你"
    return "love"

#16
init 6 python:
    import webbrowser
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaidoors271",
            category=['其他'],
            prompt="任意门2",
            conditional="store.mas_getEVL_shown_count('duhaidoors71') >= 1",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label duhaidoors271:
    m 4eub "[player],我们上次观看了{b}{i}任意门1{/i}{/b}"
    m 1hua "当看到主角学着迈克尔·杰克逊跳舞结果帽子掉的时候真的好好笑."
    m 5eub "里面一些滑稽的动作也是."
    m 6fub "现在的话，你想看看第二部吗?"
    menu:
        "我想看":
            jump duhaiwatchdoors2 

        "我现在没时间呢":
            jump duhainowatchdoors2

        "其实我还没看过第一部":
            jump duhaiohmanyoushouldlookhoney

label duhaiwatchdoors2:
    m 2fsa "好的,让我们继续看看那些作者的奇思妙想吧"
    $ webbrowser.open('https://www.bilibili.com/video/BV1qi4y1M7ZU/?spm_id_from=333.1387.search.video_card.click&vd_source=cba8ada8c24161a7b858728ed11a0e8a')
    return

label duhainowatchdoors2:
    m 1fsa "好吧,你之后如果想看的话直接给我说就好了."
    return

label duhaiohmanyoushouldlookhoney:
    m 5eub "这样啊...{w=1}不过第一部和第二部没有连贯的剧情呢,到了第三部才有."
    m 6fud "没有观看第一部不影响第二部的观看."
    m 1efa "所以,你现在想看第一部还是第二部呢?"
    menu:
        "我想看第二部":
            jump duhaiwatchdoors2

        "我想看第一部":
            jump duhaidoors1watch

        "我不太想看呢":
            jump duhainhta

label duhainhta:
    m 1efc "哦,好吧"
    m 3fua "你之后想看了跟我说声就好了喔."
    return

#17 2025/3/21 12:05
init 6 python:
    import webbrowser
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaidoors371",
            category=['其他'],
            prompt="任意门3",
            conditional="store.mas_getEVL_shown_count('duhaidoors271') >= 1",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label duhaidoors371:
    m 1eub "[player],你还记得我们上次说过的任意门吗?"
    m 2fud "各种作者的奇思妙想实在是太吸引人了,各种元素,各种风格,都在里面."
    m 6eub "我记得我们说到任意门2了,"
    m 4rua "第三部总共20分钟,但到了11分38秒开始播放的歌曲很吸引我."
    m 6hub "{b}{i}If there's one thing I could never confess~{/i}{/b}"
    m 2hua "{b}{i}It's that I can't dance a single step~{/i}{/b}"
    m 1hud "{b}{i}One thing I could never confess~{/i}{/b}"
    m 5fub "{b}{i}It's that I can't dance a single step~{/i}{/b}"
    m 1eud "如果说有件事我永远无法承认,那就是我一步都不会跳."
    m 6hua "哈哈,有点忘我了"
    m 2fua "如果你时间比较紧的话也可以从11分38秒开始看."
    m 3fub "最后百人降落阻拦主角确实震撼到我了."
    m 1eua "你现在想看看吗?"
    menu:
        "我想看":
            jump duhaiwatchdoors371

        "我现在没时间呢":
            jump duhainowatchdoors373

label duhaiwatchdoors371:
    m 5eua "嗯好,让我们一起享受吧"
    $ webbrowser.open('https://www.bilibili.com/video/BV1MK4y1e7md/?spm_id_from=333.1387.search.video_card.click&vd_source=cba8ada8c24161a7b858728ed11a0e8a')
    return

label duhainowatchdoors373:
    m 1esc "好吧,[player]"
    m 5eua "你之后想看的话跟我说一声就好了"
    return


#18 2025/3/21 12:23
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaieverythinggoeson5",
            category=['浪漫','音乐'],
            prompt="everything goes on",
            conditional="mas_canShowRisque(aff_thresh=800)",
            random=True           
        )
    )

transform piano_move:
    xpos -1.5 yalign 0.5  
    linear 5.0 xpos 0   

transform piano_return:
    xpos 0 yalign 0.5
    linear 5.0 xpos -1.5
    
label duhaieverythinggoeson5:
    m 1eua "[player],我们相识到现在,"
    extend 5hub "你给予我的爱,我都记在心里."
    m 6fubsb "为此,我特意为你学了一首歌,这是我利用了这里的钢琴和网络上的一些软件合成的,{w=1}希望你能喜欢."
    m 1eua "稍微等等."
    show monika at Transform(xpos=-800) with move
    m 2hua "我准备了好久,这下终于能派上用场————诉说我这段时间的一些感想了."
    window hide
    $ original_music = renpy.music.get_playing(channel='music')
    show mas_piano at piano_move zorder 13
    pause 5.0
    show monika at Transform(xpos=640) with move
    play music "mod_assets/music/everythinggoeson.ogg" loop fadein 2.0
    pause 150
    stop music fadeout 3.0
    show monika at Transform(xpos=-800) with move
    show mas_piano at piano_return zorder 13
    pause 5.0
    show monika at Transform(xpos=640) with move
    window show
    play music original_music fadein 2.0
    m 1hubfa "..."
    m 1esbld "我们在一起好久了,我总是免不了想到我们彼此少了对方是什么感受......"
    m 5fsblc "我只想对你说,过好当下就好了......"
    m 2hsbfb "我也会永远的爱你,永远,{w=0.5}永远都会."
    m 5eublb "爱你哦,宝宝."
    return "love"
    
    
define mas_piano = "mod_assets/images/piano.png"

#19
#2025/3/21 15:12
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaiguanju",
            category=['浪漫','莫妮卡'],
            prompt="关雎",
            random=True           
        )
    )
label duhaiguanju:
    m 1fub "{b}{i}关关雎鸠,在河之洲.{/i}{/b}"
    m 5fubld "{b}{i}窈窕淑女,君子好逑.{/i}{/b}"
    m 4fubsb "{b}{i}参差荇菜,左右流之.{/i}{/b}"
    m 6eubfb "{b}{i}窈窕淑女,寤寐求之.{/i}{/b}"
    m 2hubfd "{b}{i}求之不得,寤寐思服.{/i}{/b}"
    m 1fubfb "{b}{i}悠哉悠哉,辗转反侧.{/i}{/b}"
    m 3eubsd "{b}{i}参差荇菜,左右采之.{/i}{/b}"
    m 5fubfb "{b}{i}窈窕淑女,琴瑟友之.{/i}{/b}"
    m 2etbfd "{b}{i}参差荇菜,左右芼之.{/i}{/b}"
    m 1hubfd "{b}{i}窈窕淑女,钟鼓乐之.{/i}{/b}"
    m 6rsbla "嘿嘿..."
    m 3eubfb "这是中国最早的爱情诗之一,它展现自然之美与人性之真的结合."
    m 1fubld "前面以雎鸠和鸣起兴,引出对淑女的倾慕."
    m 6eubsa "中间以采摘荇菜喻追求过程,表现求而不得的苦闷."
    m 5hubfb "后面展示了从单相思升华到对美满婚姻的想象."
    m 2tublb "你也会想我想到辗转反侧吧,[player]?"
    menu:
        "当然,我想你想到睡不着":
            jump duhaimissyounocansleep

        "我睡得很香喔":
            jump duhaibendanzhinan

label duhaimissyounocansleep:
    m 5fubla "嘿嘿,乖宝宝,"
    m 6fubfd "我想亲亲了."
    if mas_isMoniEnamored(higher=True):
        if mas_shouldKiss:
            call monika_kissing_motion_short
    m 5hubfb "爱你哦."
    return "love"

label duhaibendanzhinan:
    m 3efp "坏孩子,[player],我不想理你了."
    m 5hublb "才不是呢,但我真拿你没办法了哈哈"
    m 1fubsb "谁让我这么爱你呢,嘿嘿"
    m 6eubsa "爱你哦."
    return "love"


image doro_png1 = im.FactorScale("Submods/Literature_and_Daily_Life/doropng/doro.png", 0.7)

#20
init 6 python:
    import webbrowser
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaidoro271",
            category=['其他','莫妮卡'],
            prompt="抽奖轮盘",
            conditional="store.mas_getEVL_shown_count('duhaidoro71') >= 1",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )             
label duhaidoro271:
    m 1eub "[player],你还记得我们说过的doro吗?"
    m 5fua "我刚刚发现了她的一个同人小视频,"
    extend 6sua "里面的人物都好可爱."
    m 3eub "嘿嘿,你现在有时间陪我一起看吗?"
    menu:
        "有呀,我很乐意和你一起看":
            jump duhailooklunpan

        "没时间呢，下次再看吧":
            jump duhainolooklunpan

label duhailooklunpan:
    m 5fub "嗯好,我现在带你看"
    $ webbrowser.open('https://www.bilibili.com/video/BV1GWCaYfEH5/?spm_id_from=333.1387.favlist.content.click')
    return

label duhainolooklunpan:
    m 1esc "哦,好吧"
    return

#21
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaidongyeguiwu",
            category=['浪漫'],
            prompt="东野圭吾",
            random=True,            
        )
    )

label duhaidongyeguiwu:
    m 4fub "宝宝,我想跟你聊聊东野圭吾."
    m 6eua "他是日本当代最具影响力的推理小说家之一,以其多变的风格,深刻的人性刻画和社会洞察力闻名."
    m 1fud "他的作品全球销量超亿册,被译成多种语言"
    m 2eua "正好我最近在阅读他的作品,我之后会跟你聊聊他的作品."
    menu:
        "好": 
             jump duhaiyessir

label duhaiyessir:
    m 1eubla "爱你"
    return "love"

#22 写到这里的这时候感觉想不到话题了,救命啊
init 6 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaibaiyexing2",
            category=['其他','莫妮卡'],
            prompt="白夜行",
            conditional="store.mas_getEVL_shown_count('duhaidongyeguiwu') >= 1",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label duhaibaiyexing2:
    m 1eua "[player],还记得我们上次谈论过的东野圭吾吗?"
    extend 5fub "我想和你谈谈他最具代表性的长篇小说之一,\"白夜行\"."
    m 6fsd "1973年,大阪发生一桩离奇命案,当铺老板桐原洋介死于废弃大楼,现场疑点重重.11岁的少年桐原亮司和同龄女孩西本雪穗成为案件的关键人物,两人的命运从此纠缠"
    m 1rua "此后19年间,雪穗与亮司表面上毫无交集,却在暗中相互依存.雪穗通过伪装,欺骗与犯罪跻身上流社会."
    m 3fub "亮司则游走于黑暗,用非法手段为她扫清障碍.但两人身边的亲友接连遭遇不幸,真相被层层掩盖."
    m 5etc "亮司与雪穗是彼此\"白夜中的光\",他们在幼年共同经历家庭扭曲,之后为了掩盖最初的罪行,他们结成扭曲的共生同盟."
    m 6fub "有趣的是,这并不是线性叙事,而是通过警察笹垣润三的追查串联碎片化事件"
    m 1eua "全书跨越19年,但并非按时间顺序展开,而是通过1973年命案与后续11个独立事件穿插叙述."
    extend 2fub "每个事件看似孤立,实际则是个巨大阴谋的齿轮."
    m 4esd "警察笹垣润三跨越19年的调查笔记成为串联碎片的核心线索,我也是到最终章才拼合起来前面的线索."
    m 6sub "这部小说实在太精彩了,我只是简要的跟你说说大致内容,我也很推荐你去读完这本书."
    m 1rua "它如同一面棱镜,折射出光明与黑暗交织的人性真相.雪穗与亮司的悲剧不仅是个体的堕落,更是社会阴影下的必然产物."
    return

#23
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaiwoheni",
            category=['浪漫','莫妮卡'],
            prompt="我和你#1",
            random=True,            
        )
    )

label duhaiwoheni:
    m 5fublb "{b}{i}晴天,有点孤单~{/i}{/b}"
    m 2hsbsd "{b}{i}玩具,丢在旁边~{/i}{/b}"
    m 1fubfb "{b}{i}电视里没有新鲜~{/i}{/b}"
    extend 6eubfd "{b}{i}球鞋跑不过时间~{/i}{/b}"
    m 3fubfb "{b}{i}我要更大的世界,装满不同的探险~{/i}{/b}"
    menu:
        "当然你陪在身边.":
             jump duhaiyouandmesongs

label duhaiyouandmesongs:
    m 5fubfb "{b}{i}每秒每天~{/i}{/b}"
    m 1fubfa "{b}{i}我和你飞到蓝蓝的天边,我和你种下满满的花园~{/i}{/b}"
    menu:
        "我和你分享暖暖的光线":
             jump duhaiyouandmesong

label duhaiyouandmesong:
    m 6eublb "{b}{i}再靠近一点~{/i}{/b}"
    m 3fubsd "{b}{i}我和你就像蓝蓝的天边,{w=2}我和你就像满满的花园~{/i}{/b}"
    m 1eubsb "{b}{i}我和你就像暖暖的光线,{w=2}把地球照亮~{/i}{/b}"
    m 2fublb "{b}{i}再靠近一点~{/i}{/b}"
    menu:
        "再靠近一点":
             jump duhaizaikaojinyidian

label duhaizaikaojinyidian:
    m 5fubfb "再靠近一点,{w=1.5}再靠近一点"
    m 6rubla "..."
    m 1fublb "这首歌确实很好听呢,[player]."
    m 6eubld "而且这个动画里面的角色也很可爱,比如说阿呦和桃酥"
    m 2fubfb "每每听到这首歌,我都很怀念我和你的经历."
    m 1eubld "让我们继续向前走,好吗?"
    return

#24
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhailuxun2",
            category=['浪漫'],
            prompt="鲁迅",
            random=True,            
        )
    )
label duhailuxun2:
    m 1eua "[player],我想和你谈谈鲁迅"
    m 5fub "他是中国现代文学的奠基人之一,也是20世纪最具影响力的思想家,作家和社会批评家.他以犀利的文笔,深刻的社会批判和人文关怀闻名"
    m 3esa "开创白话小说新范式,语言风格冷峻犀利被誉为\"中国现代文学之父\"."
    m 6huc "鲁迅的思想在今天仍具现实意义,"
    extend 2eub "他的文字如同一面镜子,照见每个时代的精神困境."
    m 5eua "我之后会和你聊聊他的一些作品"
    return

#25
init 6 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaiacyshj1",
            category=['文学','莫妮卡'],
            prompt="朝花夕拾(阿长与山海经)",
            conditional="store.mas_getEVL_shown_count('duhailuxun2') >= 1",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label duhaiacyshj1:
    m 5fua "嘿,[player]"
    m 1ftb "还记得我们上次说的作家鲁迅吗?"
    m 2rud "我想和你聊聊他唯一一部回忆性散文集,\"朝花夕拾\"."
    m 6fub "这部作品以个人成长经历为线索,既充满对童年往事的温情追忆."
    extend 1fua "又贯穿着对封建文化的深刻批判,堪称中国现代散文的典范之作."
    m 4fub "下面我和你讲讲其中的\"阿长与《山海经》\"."
    m 5eua "对于阿长,鲁迅在开始是这么描写的"
    m 1fud "她生得黄胖而矮...{w=1}最讨厌的是常喜欢切切察察,向人们低声絮说些什么事."
    m 2eub "通过\"睡相成'大'字\"和\"逼鲁迅吃福橘\"等等，构建粗俗可笑的初印象."
    m 5fua "但在阿长买来\"三哼经\"之后,鲁迅对于她的态度便改变了."
    menu:
        "三哼经?":
             jump duhaisanhenjing

label duhaisanhenjing:
    m 6fub "嘿嘿,这应该是方言之类的?吧山海经说成三哼经了."
    m 2eub "其中阿长还陪鲁迅一起抓蟋蟀,可以说她给予了鲁迅很多的温暖"
    m 1fua "当私塾先生教\"《鉴略》\"时，小鲁迅\"却只默默地静听着\",那是被规训的沉默."
    m 4fsd "而阿长送来绘图本时,\"我似乎遇着了一个霹雳,全体都震悚起来\",这才是知识应有的震撼力.粗粝的木刻版画,经由文盲的手,反而比精装典籍更接近文化真髓."
    m 2ftc "阿长去世时的笔触,鲁迅处理得极轻又极重."
    m 6rsb "\"我的保姆,长妈妈即阿长,辞了这人世,大概也有了三十年了罢.我终于不知道她的姓名,她的经历,仅知道有一个过继的儿子,她大约是青年守寡的孤孀.\""
    m 1fua "那个教你除夕规矩,给你买神话书,陪你度过童年的至亲之人,竟连全名都湮没在时光里."
    m 5ltd "那些未被言说的细节更耐寻味,她何时去世?病痛中可有人照料?这些留白像极了民间丧仪上被风吹散的纸钱灰."
    m 6eub "底层人的生死,原就轻飘如草芥.但正是这般克制的书写,让阿长这个无名者,在文学史中获得了比无数达官显贵更恒久的姓名."
    m 1fua "真的好精彩,我希望在我讲完之后你能看一下这极具温情的篇章.{w=1.5}我也希望你能够珍惜身边对你好的人"
    m 2eub "爱你."
    return "love"

#26
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaihuangyeduju",
            category=['其他','莫妮卡'],
            prompt="荒野独居",
            random=True,
        )
    )

label duhaihuangyeduju:
    m 5eub "[player],你之前看过{b}{i}荒野独居{/i}{/b}这个节目吗."
    m 1wud "这个节目在每一季都会邀请拥有野外求生经验的人来参与竞争,坚持到最后的人便会获得巨额奖金."
    m 2eua "我最近在睡觉前总是会看一会,毕竟这种类型的节目确实很吸引人."
    m 3fub "在比赛中还有人通过钓鱼和制作陷阱来获取食物,更有人通过猎杀大型动物豪取冠军."
    m 6hua "也有人在建好自己的\"荒野豪宅\"后便退赛,对此有人认为他们应该去参加\"荒野建造大赛\",哈哈."
    m 1euc "有的人拥有实力却因为忍受不了孤独感,止不住对亲人的思念而选择退出比赛,真的很可惜."
    m 5rtd "我在观看的同时也在想,如果我去参加这个节目的话会怎么样呢?"
    m 1fublb "不对,我可能才落地不到一天就想回来见你了."
    m 6fubla "因为我是真的好想你,好想你,好想你."
    extend 2hubfb "止不住地想."
    m 1eubfb "希望你也能这么想我,嘿嘿"
    m 5fubfa "爱你"
    return "love"



#27
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaigangqinlianxi",
            category=['音乐'],
            prompt="练习钢琴",
            random=True,
        )
    )

label duhaigangqinlianxi:
    m 1eub "嘿,[player]."
    extend 5fua "我最近在网络上发现了很多首曲子,它们旋律让我赞不绝口."
    m 3fublb "我也打算学习一下,然后弹给你听"
    m 2eubla "同时我发现了一些音乐软件,它们居然能发出各种乐器的声音."
    m 1eub "这让我有了想试试合成音乐的想法."
    m 6fubla "如果将钢琴和其他乐器结合起来的效果足够好的话."
    m 1hubfb "我很乐意分享给你"
    m 5fubla "在此之前,给我些时间准备准备吧,宝宝."
    m 2hublb "毕竟,{w=1.5}作为你的女友,我当然是选择和你一起进步呀."
    return

#28
init 6 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaiqueqiaoxian",
            category=['浪漫'],
            prompt="《鹊桥仙・纤云弄巧》",
            conditional="mas_canShowRisque(aff_thresh=400)",
            random=True
        )
    )

label duhaiqueqiaoxian:
    m 5fua "{b}{i}纤云弄巧,飞星传恨,{/i}{/b}"
    extend 2fud "{b}{i}银汉迢迢暗度,{/i}{/b}"
    m 6sublb "{b}{i}金风玉露一相逢,便胜却人间无数.{/i}{/b}"
    m 1hubla "{b}{i}柔情似水,佳期如梦,{/i}{/b}"
    extend 5hublb "{b}{i}忍顾鹊桥归路{/i}{/b}"
    m 6fubfa "{b}{i}两情若是久长时{/i}{/b}"
    menu:
        "又岂在朝朝暮暮":
             jump queqiaoxianforeverlove

label queqiaoxianforeverlove:
    m 1hubfa "..."
    m 5fublb "我真得很喜欢这首诗呢,[player]"
    m 2eubld "它打破\"欢娱苦短\"的哀婉基调，以\"金风玉露一相逢,便胜却人间无数\"歌颂超越时空的真爱,强调爱情的忠贞与精神共鸣."
    m 3rubfb "结尾的\"两情若是久长时,又岂在朝朝暮暮\",将爱情提升至超越世俗聚散的哲学高度."
    m 6fubla "神话与现实交织,使作品兼具文学美感与思想深度."
    extend 1hubsb "成为中国古典爱情诗词中\"永恒与超越\"主题的典范."
    m 2esa "有时你忙于生活的事情,来陪我的时间变少了,"
    extend 5fubfb "我也能理解"
    m 1hubla "但我希望我们并不因为陪伴的减少而逐渐丧失对对方的热情."
    m 5fubfb "我爱你."
    return "love"

#29
init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="dushenbianyouni",
            prompt="有你在我身边,真好!",
            unlocked=True
        ),
        code="CMP"
    )

label dushenbianyouni:
    m 2hubla "嘿嘿."
    m 5tublu "你能这么说,我真的很开心~"
    m 7eublb "嗯,{w=1}我也想对你这么说...{w=1}毕竟我们相互治愈着."
    m 1fubfa "希望我们能好好地走下去."
    return 

    




         
        











             
    





     
    
            

