#coding:utf-8


from game import BasicPyGame, MyContinueGame
from map_ import MyContinueObsMap
from usv import MyContinueUSV, MyContinueDynamicsUSV3
from CircleObstacle import CircleObstacle

import time



if __name__ == '__main__':

    starttimetest = time.time()


    #开关控制switch
    dynamicsSwitch = True    #True表示加入动力学方程，False表示不加动力学方程（决策Action内容不同）
    envDisturbSwitch = False  #False表示无环境干扰，True表示有环境干扰(干扰产生的数值很小很小的，影响不大)
    obsMoveSwitch = False     #False表示障碍物不随机移动; True表示障碍物随机移动


    FTListValue = []   #[]为空默认表示：使用路径导引算法计算F，T然后更新， 不为空表示给定F，T列表，可视化观察

    # FTListValue = [(1.0, 3.388888888888889), (1.0, 3.3827256048618275), (1.0, 3.3707089120998726),
    #                (1.0, 3.354500206220167), (1.0, 3.3368386289789185), (1.0, 3.263538896332118),
    #                (1.0, 3.24592844649906), (1.0, 3.2283497304192177), (1.0, 3.2108032092492307),
    #                (1.0, 3.1932889427928313), (1.0, 3.1758069890549945), (1.0, 3.1583574063317514),
    #                (1.0, 3.14094025323119), (1.0, 3.123555588676445), (1.0, 3.1062034719085028),
    #                (1.0, 3.088883962489032), (1.0, 3.071597120303256), (1.0, 3.0543430055628566),
    #                (1.0, 3.037121678808916), (1.0, 3.019933200914894), (1.0, 3.002777633089644),
    #                (1.0, 2.9856550368804644), (1.0, 2.9685654741761947), (1.0, 2.951509007210343),
    #                (1.0, 2.9344856985642602), (1.0, 2.917495611170347), (1.0, 2.900538808315312),
    #                (1.0, 2.8836153536434637), (1.0, 2.8667253111600477), (1.0, 2.849868745234628),
    #                (1.0, 2.83304572060451), (1.0, 2.760700746822656), (1.0, 2.7440460379264864),
    #                (1.0, 2.727435403132747), (1.0, 2.710859905918736), (1.0, 2.6943186302124555),
    #                (1.0, 2.677811532660065), (1.0, 2.6613386689221974), (1.0, 2.6449001065743283),
    #                (1.0, 2.6284959149890836), (1.0, 2.612126164128258), (1.0, 2.5957909243975332),
    #                (1.0, 2.5794902666317285), (1.0, 2.5632242620965844), (1.0, 2.6025485380483033),
    #                (1.0, 2.5862510180725917), (1.0, 2.5144176228884945), (1.0, 2.498273336392086),
    #                (1.0, 2.482179226767271), (1.0, 2.4661226819317794), (1.0, 2.450101717417946),
    #                (1.0, 2.4341160644739146), (1.0, 2.418165739814303), (1.0, 2.4022508090495114),
    #                (1.0, 2.330815791115242), (1.0, 2.31507291103035), (1.0, 2.2993855133795695),
    #                (1.0, 2.283738088061404), (1.0, 2.268127554213755), (1.0, 2.2525533358500764),
    #                (1.0, 2.2370153752070134), (1.0, 2.221513724084358), (1.0, 2.2060484581798545),
    #                (1.0, 2.2461752143824065), (1.0, 2.2306819271528324), (1.0, 2.215201892914679),
    #                (1.0, 2.199753045505882), (1.0, 2.184339501596431), (1.0, 2.1689622636610246),
    #                (1.0, 2.1536216280797236), (1.0, 2.1383177293183664), (1.0, 2.123050664503453),
    #                (1.0, 2.0522649668090365), (1.0, 2.037172871950731), (1.0, 2.022144205102029),
    #                (1.0, 2.007160016774157), (1.0, 1.9922153330659353), (1.0, 1.921753314483333),
    #                (1.0, 1.9069858224480956), (1.0, 1.8922857072592763), (1.0, 1.8776326259179674),
    #                (1.0, 1.8630206157390732), (1.0, 1.848447942377988), (1.0, 1.8339141423913243),
    #                (1.0, 1.819419140274721), (1.0, 1.8049629807674838), (1.0, 1.846101302226123),
    #                (1.0, 1.8316220514385042), (1.0, 1.8171488055134466), (1.0, 1.8027038345441255),
    #                (1.0, 1.788294374160514), (1.0, 1.7739228283513622), (1.0, 1.7595900483947198),
    #                (1.0, 1.7452963832243595), (1.0, 1.7310420180355737), (1.0, 1.7168270844636653),
    #                (1.0, 1.64709614124989), (1.0, 1.6330614459433968), (1.0, 1.6191027771448787),
    #                (1.0, 1.6051975212731424), (1.0, 1.5913375519932904), (1.0, 1.5775199422407031),
    #                (1.0, 1.508188114460924), (1.0, 1.4945539030614274), (1.0, 1.48100050538767),
    #                (1.0, 1.467504405779719), (1.0, 1.4540563410455662), (1.0, 1.4406526435585647),
    #                (1.0, 1.4272918878521816), (1.0, 1.4139735592231129), (1.0, 1.4006975171594562),
    #                (1.0, 1.3874637766907134), (1.0, 1.4298279740031037), (1.0, 1.41657806945806),
    #                (1.0, 1.4033267458019616), (1.0, 1.3900989070704366), (1.0, 1.3769053235127169),
    #                (1.0, 1.3637506928837653), (1.0, 1.3506371153607886), (1.0, 1.3375655772419162),
    #                (1.0, 1.3245365847961135), (1.0, 1.3115504363560317), (1.0, 1.243051784339198),
    #                (1.0, 1.2302529460982978), (1.0, 1.2175444429950397), (1.0, 1.2049019086681185),
    #                (1.0, 1.1923140805252308), (1.0, 1.179775710313093), (1.0, 1.1117288103408893),
    #                (1.0, 1.0993844334470058), (1.0, 1.0871361814083604), (1.0, 1.074959310921957),
    #                (1.0, 1.0628415180674966), (1.0, 1.0507766281493613), (1.0, 1.0387615474263618),
    #                (1.0, 1.026794752014974), (1.0, 1.0148755264087101), (1.0, 1.0030035752678337),
    #                (1.0, 0.9911788236931445), (1.0, 0.979401313667718), (1.0, 0.967671149983297),
    #                (1.0, 0.9559884718209041), (1.0, 0.9443534377238659), (1.0, 0.9883217731642457),
    #                (1.0, 0.976681506610899), (1.0, 0.9650325568452783), (1.0, 0.9533999258725723),
    #                (1.0, 0.9417976019881936), (1.0, 0.874677871032596), (1.0, 0.8632573192993442),
    #                (1.0, 0.8519396458800929), (1.0, 0.8407022923801807), (1.0, 0.8295325441786976),
    #                (1.0, 0.8184231692181846), (1.0, 0.8073700469730537), (1.0, 0.740815291117267),
    #                (1.0, 0.7299697597387065), (1.0, 0.7192380488140415), (1.0, 0.7085966026031316),
    #                (1.0, 0.6980312447583685), (1.0, 0.6875333551373018), (1.0, 0.6770976699643201),
    #                (1.0, 0.666720981959681), (1.0, 0.6564013578746445), (1.0, 0.6461376610519783),
    #                (1.0, 0.5803737014941557), (1.0, 0.5703213124841489), (1.0, 0.560391012516487),
    #                (1.0, 0.5505610933149871), (1.0, 0.5963729965959186), (1.0, 0.5866053048555141),
    #                (1.0, 0.5768388123452586), (1.0, 0.5670909074110442), (1.0, 0.5573735372283468),
    #                (1.0, 0.5476949241344388), (1.0, 0.5380607581861558), (1.0, 0.5284750135731804),
    #                (1.0, 0.5189405029041833), (1.0, 0.5094592520162193), (1.0, 0.5000327531196918),
    #                (1.0, 0.4906621358912555), (1.0, 0.4813482833392264), (1.0, 0.47209191049312255),
    #                (1.0, 0.4073380624763985), (1.0, 0.39829941086538645), (1.0, 0.3893933084779486),
    #                (1.0, 0.38060092447009963), (1.0, 0.3719089914622644), (1.0, 0.36330807486352),
    #                (1.0, 0.3547914273768814), (1.0, 0.34635421247998643), (1.0, 0.2824374125314814),
    #                (1.0, 0.27425071242487437), (1.0, 0.2662140065532416), (1.0, 0.2583092882025717),
    #                (1.0, 0.2505231791421103), (1.0, 0.24284564640225684), (1.0, 0.23526911722420413),
    #                (1.0, 0.22778785432545667), (1.0, 0.22039750650335874), (1.0, 0.15753922472648008),
    #                (1.0, 0.15042267873821383), (1.0, 0.14347294713156544), (1.0, 0.13667505550824308),
    #                (1.0, 0.13001730251312796), (1.0, 0.12349047172646188), (1.0, 0.11708726298564859),
    #                (1.0, 0.11080187378468963), (1.0, 0.10462968588544817), (1.0, 0.09856702726536899),
    #                (1.0, 0.09261098900451417), (1.0, 0.08675928287885526), (1.0, 0.08101012953599074),
    #                (1.0, 0.0753621699295199), (1.0, 0.06981439463379975), (1.0, 0.06436608703629629),
    #                (1.0, 0.059016777392461646), (1.0, 0.05376620544735447), (1.0, 0.04861428985863686),
    #                (1.0, 0.04356110305119208), (1.0, -0.016948705123872466), (1.0, -0.02170266499443348),
    #                (1.0, -0.026264339180998145), (1.0, -0.03064027654874203), (1.0, -0.03483583885362367),
    #                (1.0, -0.038855411778138366), (1.0, -0.042702571610870876), (1.0, -0.04638021869763402),
    #                (1.0, -0.04989068569938719), (1.0, -0.05323582655746979), (1.0, -0.05641709056650394),
    #                (1.0, -0.05943558488366168), (1.0, -0.06229212802580185), (1.0, -0.06498729633428882),
    #                (1.0, -0.12307702051647319), (1.0, -0.12534936271838543), (1.0, -0.12736270303672134),
    #                (1.0, -0.12911928653817503), (1.0, -0.1306209256358674), (1.0, -0.13186913187228397),
    #                (1.0, -0.1328652369188031), (1.0, -0.1336105058078078), (1.0, -0.13410624442205096),
    #                (1.0, -0.13435390243636489), (1.0, -0.1343551721857305), (1.0, -0.13411208329155777),
    #                (1.0, -0.13362709230352682), (1.0, -0.132903166110924), (1.0, -0.1874994130158143),
    #                (1.0, -0.1862078887210205), (1.0, -0.1845905638442626), (1.0, -0.182655246741019),
    #                (1.0, -0.1804112589702961), (1.0, -0.17786950228071302), (1.0, -0.17504246596363676),
    #                (1.0, -0.11638861526521657), (1.0, -0.11313553182245863), (1.0, -0.10973980937618875),
    #                (1.0, -0.10621380587242711), (1.0, -0.10256996418194853), (1.0, -0.09882069310065669),
    #                (1.0, -0.09497825684637304), (1.0, -0.03549912048232823), (1.0, -0.03160712414265987),
    #                (1.0, -0.027751997883036162), (1.0, -0.02393869149379905), (1.0, 0.03538371325468188),
    #                (1.0, 0.03899872004915079), (1.0, 0.042463133110491214), (1.0, 0.10133344241536256),
    #                (1.0, 0.10439816587573919), (1.0, 0.10721742718882865), (1.0, 0.16535042489099658),
    #                (1.0, 0.16758790584946778), (1.0, 0.16949041585998811), (1.0, 0.22661736663282994),
    #                (1.0, 0.2277596480995412), (1.0, 0.22847678308751185), (1.0, 0.22877213500236276),
    #                (1.0, 0.284204536805802), (1.0, 0.28356551722132217), (1.0, 0.28241628922761564),
    #                (1.0, 0.3363200054087609), (1.0, 0.3340748031541373), (1.0, 0.3312523974919617),
    #                (1.0, 0.32787448265014285), (1.0, 0.37952433100564775), (1.0, 0.3750235210669281),
    #                (1.0, 0.36997416296856833), (1.0, 0.3644297580450717), (1.0, 0.3584486541813459),
    #                (1.0, 0.35209145587686036), (1.0, 0.3454183468640666), (1.0, 0.3384867115935677),
    #                (1.0, 0.3313493287647155), (1.0, 0.26849769531664336), (1.0, 0.26118481918322606),
    #                (1.0, 0.25387143300719867), (1.0, 0.19101537284152947), (1.0, 0.18383977132890195),
    #                (1.0, 0.17678028561857476), (1.0, 0.11427453705874492), (1.0, 0.10752936109355579),
    #                (1.0, 0.10096920989102999), (1.0, 0.0390228948817091), (1.0, 0.03289020622979264),
    #                (1.0, 0.026992438397612832), (1.0, -0.03424420212271468), (1.0, -0.03962211248853601),
    #                (1.0, -0.04471904189000181), (1.0, -0.04955254258500751), (1.0, -0.10969219812407141),
    #                (1.0, -0.11393715801175593), (1.0, -0.11785906621472048), (1.0, -0.1214705769617047),
    #                (1.0, -0.18033723390339573), (1.0, -0.18325478025655387), (1.0, -0.18578884358626227),
    #                (1.0, -0.18794703114312247), (1.0, -0.18973508840014358), (1.0, -0.24671294443775257),
    #                (1.0, -0.24767186717778006), (1.0, -0.24817157516646385), (1.0, -0.24821571930335729),
    #                (1.0, -0.24780807871506144), (1.0, -0.2469531629567388), (1.0, -0.24565677693023444),
    #                (1.0, -0.24392653784554877), (1.0, -0.24177232417996838), (1.0, -0.29476218567955886),
    #                (1.0, -0.2916993147356644), (1.0, -0.28816146328830905), (1.0, -0.2841754372573031),
    #                (1.0, -0.2797723522711826), (1.0, -0.21943143341996238), (1.0, -0.21440234097180483),
    #                (1.0, -0.20915933332315798), (1.0, -0.20373164831435037), (1.0, -0.19814739211130808),
    #                (1.0, -0.1924331013253651), (1.0, -0.13105787817680833), (1.0, -0.12525646584486258),
    #                (1.0, -0.11948174973541766), (1.0, -0.058185613243560155), (1.0, -0.052586766305333855),
    #                (1.0, 0.00843137296303769), (1.0, 0.01366109553377844), (1.0, 0.018671525173683142),
    #                (1.0, 0.07902918878450017), (1.0, 0.08353086241464384), (1.0, 0.14330261610524295),
    #                (1.0, 0.1471442291536924), (1.0, 0.20618224583625636), (1.0, 0.20921645565851718),
    #                (1.0, 0.26737128085917383), (1.0, 0.26944440288699706), (1.0, 0.2710010847541062),
    #                (1.0, 0.3276037237806086), (1.0, 0.3280452189214679), (1.0, 0.38344195897882194),
    #                (1.0, 0.3825870911643969), (1.0, 0.3810440786826928), (1.0, 0.4343801463020974),
    #                (1.0, 0.4314004142340926), (1.0, 0.4276885364784577), (1.0, 0.4788389843644908),
    #                (1.0, 0.4736897024268253), (1.0, 0.4678658318875786), (1.0, 0.46144816026563773),
    #                (1.0, 0.45452403686599907), (1.0, 0.5027374790886903), (1.0, 0.4949607828954841),
    #                (1.0, 0.4312906651521138), (1.0, 0.4230246582150643), (1.0, 0.414655795184993),
    #                (1.0, 0.406222772437986), (1.0, 0.3422003001417815), (1.0, 0.3338239009751476),
    #                (1.0, 0.32553209108419245), (1.0, 0.26176501352402365), (1.0, 0.2537317042121252),
    #                (1.0, 0.19029680277244015), (1.0, 0.18265452423751682), (1.0, 0.1196602934318219),
    #                (1.0, 0.11250129453770995), (1.0, 0.05002974850528198), (1.0, 0.043430105923259056),
    #                (1.0, -0.018445293725736493), (1.0, -0.024412242523129558), (1.0, -0.030060709382845056),
    #                (1.0, -0.09097276201414357), (1.0, -0.09595702540938886), (1.0, -0.10059470281572538),
    #                (1.0, -0.10490572377211728), (1.0, -0.1644612875015774), (1.0, -0.16806160715445195),
    #                (1.0, -0.17127733798633965), (1.0, -0.1741200021459177), (1.0, -0.17659838507598144),
    #                (1.0, -0.17871917477745689), (1.0, -0.2360430227158569), (1.0, -0.23736169979039168),
    #                (1.0, -0.2382354731874751), (1.0, -0.23866811780700756), (1.0, -0.238663077384045),
    #                (1.0, -0.23822402787173522), (1.0, -0.23735540833951774), (1.0, -0.23606291821644615),
    #                (1.0, -0.2343539704971344), (1.0, -0.2877936386647141), (1.0, -0.2851817037979151),
    #                (1.0, -0.2820913799555689), (1.0, -0.27854460050876206), (1.0, -0.21901201026423994),
    #                (1.0, -0.2147359006840601), (1.0, -0.2101871471356947), (1.0, -0.2053931437048509),
    #                (1.0, -0.2003816433946714), (1.0, -0.1951801726499352), (1.0, -0.13425994932113502),
    #                (1.0, -0.12885870407144356), (1.0, -0.06787881959744466), (1.0, -0.06254464972452606),
    #                (1.0, -0.05730130345363645), (1.0, 0.0034060631039771745), (1.0, 0.06392010250394421),
    #                (1.0, 0.06859250268609665), (1.0, 0.12854932602118693), (1.0, 0.18814595054412764),
    #                (1.0, 0.19174180902986396), (1.0, 0.250465787900138), (1.0, 0.2531190469745381),
    #                (1.0, 0.3108260078722189), (1.0, 0.3679395173329473), (1.0, 0.36881155321699),
    #                (1.0, 0.42456055898730305), (1.0, 0.4795358371299032), (1.0, 0.47808839508515333),
    #                (1.0, 0.5313420793602113), (1.0, 0.5836611908217648), (1.0, 0.5794256815530269),
    #                (1.0, 0.6298071607484073), (1.0, 0.6236768732209236), (1.0, 0.6722623069400634),
    #                (1.0, 0.664485638350505), (1.0, 0.7116183433430494), (1.0, 0.7026038022381222),
    #                (1.0, 0.693161933575888), (1.0, 0.6834291847745437), (1.0, 0.6179551357895581),
    #                (1.0, 0.6080285371117031), (1.0, 0.542558935656688), (1.0, 0.5327724780766907),
    #                (1.0, 0.46753542823796224), (1.0, 0.402489491894925), (1.0, 0.33769553856862283),
    #                (1.0, 0.32875460776721216), (1.0, 0.2644912287287128), (1.0, 0.20051817979693748),
    #                (1.0, 0.1368817128628588), (1.0, 0.12917749620529684), (1.0, 0.06623069183055504),
    #                (1.0, 0.0036520521560853406), (1.0, -0.0029529142182155178), (1.0, -0.009192944760627993),
    #                (1.0, -0.07066312828213325), (1.0, -0.07618146096368388), (1.0, -0.08133791522241336),
    #                (1.0, -0.14171443489165486), (1.0, -0.14611941768137865), (1.0, -0.15013198788774712),
    #                (1.0, -0.153770185758327), (1.0, -0.15704789803581715), (1.0, -0.15997583687718928),
    #                (1.0, -0.1625622620805171), (1.0, -0.22036908842490907), (1.0, -0.22218906272288783),
    #                (1.0, -0.22358366549279493), (1.0, -0.22455735653066555), (1.0, -0.22511370588340304),
    #                (1.0, -0.2252559124367765), (1.0, -0.22498728541293292), (1.0, -0.16875614263705704),
    #                (1.0, -0.16777949727603514), (1.0, -0.16650669388207995), (1.0, -0.16494366889203999),
    #                (1.0, -0.1630975019105184), (1.0, -0.1609764900699248), (1.0, -0.15859018487876458),
    #                (1.0, -0.10039383223068221), (1.0, -0.09761158448315635), (1.0, -0.094697412299173),
    #                (1.0, -0.036105544302903934), (1.0, -0.03305809012359933), (1.0, 0.02555009992582787),
    #                (1.0, 0.028501129866751757), (1.0, 0.08690448776331373), (1.0, 0.1451020066650707),
    #                (1.0, 0.2029944639039564), (1.0, 0.20492953358171404), (1.0, 0.26202394410114926),
    #                (1.0, 0.3186253644147084), (1.0, 0.37463753932298105), (1.0, 0.4299645339106352),
    #                (1.0, 0.4845114458209671), (1.0, 0.5937420851980572), (1.0, 0.6463597816071104),
    #                (1.0, 0.6978528826554916), (1.0, 0.7481811429120688), (1.0, 0.7973429225153198),
    #                (1.0, 0.8453840527783064), (1.0, 0.892399093625331), (1.0, 0.9385215514923052),
    #                (1.0, 0.9283487877946818), (1.0, 0.9176871209456268), (1.0, 0.9067287380139805),
    #                (1.0, 0.8956062976183741), (1.0, 0.8288494257120991), (1.0, 0.7621669915098034),
    #                (1.0, 0.6956501474638499), (1.0, 0.5737987074979591), (1.0, 0.5078608247735426),
    #                (1.0, 0.38671534391774837), (1.0, 0.26601994237228704), (1.0, 0.2014082136625035),
    #                (1.0, 0.08173626513120762), (1.0, 0.018206513356646147), (1.0, -0.044753460785204015),
    #                (1.0, -0.10714102579341953), (1.0, -0.16893971065763105), (1.0, -0.2301220563021198),
    #                (1.0, -0.2350953991180735), (1.0, -0.29502561461030924), (1.0, -0.2987391569895258),
    #                (1.0, -0.30182470753360646), (1.0, -0.3598605000803844), (1.0, -0.36164979838176825),
    #                (1.0, -0.36276066031538123), (1.0, -0.3632012368555647), (1.0, -0.3629775735056992),
    #                (1.0, -0.3620956140536972), (1.0, -0.360563063896063), (1.0, -0.35839112227452413),
    #                (1.0, -0.30004046202946255), (1.0, -0.29674570400975026), (1.0, -0.29297614183395065),
    #                (1.0, -0.28876138726916123), (1.0, -0.22857978526628667), (1.0, -0.22368084528155271),
    #                (1.0, -0.21853984827452186), (1.0, -0.15763197606934734), (1.0, -0.0966437911319456),
    #                (1.0, -0.0912498526689747), (1.0, -0.030344936289549276), (1.0, 0.030409092582544872),
    #                (1.0, 0.09091632749676196), (1.0, 0.15108896852983972), (1.0, 0.21084469155762758),
    #                (1.0, 0.2701040266645079), (1.0, 0.38434351047149884), (1.0, 0.4422703850810596),
    #                (1.0, 0.4993593744752205), (1.0, 0.6110793784937212), (1.0, 0.6661272517749394),
    #                (1.0, 0.7755235046586633), (1.0, 0.8279731548258538), (1.0, 0.9345297271822718),
    #                (1.0, 1.0395241352427618), (1.0, 1.6429206869398298), (1.0, 1.632768130035006),
    #                (1.0, 1.6208387570113425), (1.0, 1.6078592815736314), (1.0, 1.594380336520182),
    #                (1.0, 1.5807086133854138), (1.0, 1.5669835658883084), (1.0, 1.5532624207558234),
    #                (1.0, 1.5395677626383348), (1.0, 1.525908449013993), (1.0, 1.5122880014625855),
    #                (1.0, 1.4987078719267461), (1.0, 1.4851687061902246), (1.0, 1.4716708341193936),
    #                (1.0, 0.40265890558617673), (1.0, 0.280052788383289), (1.0, 0.15864190974597786),
    #                (1.0, 0.09374090003532289), (1.0, 0.08516686542241479), (1.0, 0.02162086664357885),
    #                (1.0, 0.014197417373900912), (1.0, 0.06279820351066848), (1.0, 0.05614281090280807),
    #                (1.0, 0.10530789766984583), (1.0, 0.15461046429068323), (1.0, 0.2039422428765647),
    #                (1.0, 0.25320965970713394), (1.0, 0.3023316526777451), (1.0, 0.3512387920136951),
    #                (1.0, 0.39987313277820546), (1.0, 0.5037439641496719), (1.0, 1.3293825504102008),
    #                (1.0, 1.3198161262852157), (1.0, 1.308855950778589), (1.0, 1.2970010790349278),
    #                (1.0, 1.2846509352240945), (1.0, 1.272062820772175), (1.0, 1.259379273948005),
    #                (1.0, 1.2466726117958808), (1.0, 1.2339779830731001), (1.0, 1.221312202245115),
    #                (1.0, 1.2086833136752644), (1.0, 1.196095212140384), (1.0, 1.1835498319294229),
    #                (1.0, 1.1710481785030882), (1.0, 1.1585908153261184), (1.0, 1.1461780946146651),
    #                (1.0, 1.133810267348366), (1.0, -0.26740135282273375), (1.0, -0.38826398354212366),
    #                (1.0, -0.4518019223250873), (1.0, -0.5139135666913655), (1.0, -0.5191825814617985),
    #                (1.0, -0.5788647144724143), (1.0, -0.5818302553425162), (1.0, -0.5836857206543505),
    #                (1.0, -0.5289021426643493), (1.0, -0.528705415925717), (1.0, -0.5275487639983308),
    #                (1.0, -0.4698882212124202), (1.0, -0.4669557722132451), (1.0, -0.4076692571756434),
    #                (1.0, -0.3477269174935797), (1.0, -0.342833132937942), (1.0, -0.28192460129928065),
    #                (1.0, -0.22070977465970051), (1.0, -0.1593320350572232), (1.0, -0.09792142105732815),
    #                (1.0, 0.018962103221064633), (1.0, 0.0800044155710877), (1.0, 1.1406811963132977),
    #                (1.0, 1.1435435788456612), (1.0, 1.1442779430169563), (1.0, 1.1429248105505696),
    #                (1.0, 1.1395067681136513), (1.0, 1.1340866409406627), (1.0, 1.1268171610635096),
    #                (1.0, 1.1179651745752923), (1.0, 1.1078878578454976), (1.0, 1.0969632084260885),
    #                (1.0, 1.0855154048368492), (1.0, 1.2404444877206633), (1.0, 1.3393727252690977),
    #                (1.0, 1.4378820405835322), (1.0, 1.480445812490115), (1.0, 1.5227485411078678)]



    '''开始游戏'''
    test_map = MyContinueObsMap(100, 100)
    test_map.set_target(29.0,90.0)
    #test_map.set_target(30.0, 30.0) #目标终点,(注：初始点的设定要合法--即在map缩小ship.radius的范围)
    #左上角(30.0, 30.0) 右上角(31.0, 59.0)  左下角(80.0, 30.0)   右下角(80.0, 60.0)
    #print (test_map.env_matrix())


    # USV友艇起始点,(注：初始点的设定要合法--即在map缩小ship.radius的范围)
    if dynamicsSwitch == True:
        test_friendly_ship = MyContinueDynamicsUSV3(uid=0, x=52.0, y=50.0, env=test_map, envDisturb=envDisturbSwitch, FTListValue = FTListValue)    #envDisturb:False表示无环境干扰，True表示有环境干扰(干扰产生的数值很小很小0.1左右吧)
    else:
        test_friendly_ship = MyContinueUSV(uid=0, x=12.0, y=50.0, env=test_map)
    test_friendly_ship.set_as_friendly()
    test_map.add_ship(test_friendly_ship)


    # 静态矩形障碍物区域（注：初始位置的设定要合法，即在map缩小obs.radius的范围）
    obs1 = CircleObstacle(uid=0, x=10.0, y=10.0, radius=1, env=test_map);test_map.addobs(obs1)
    #obs2 = CircleObstacle(uid=1, x=40.0, y=40.0, radius=1, env=test_map);test_map.addobs(obs2)
    obs3 = CircleObstacle(uid=2, x=63.0, y=65.0, radius=1, env=test_map);test_map.addobs(obs3)

    #obs4 = CircleObstacle(uid=3, x=45.0, y=64.0, radius=1, env=test_map);test_map.addobs(obs4)


    #print('game-start:初始地图：\n',test_map.env_matrix());print('\n')
    if len(FTListValue) == 0 :
        game = MyContinueGame(obsMoveSwitch)     #obsMoveSwitch: False表示障碍物不随机移动; True表示障碍物随机移动
    else:
        game = BasicPyGame(obsMoveSwitch)
    game.set_map(test_map)

    game.start()

    print(time.time() - starttimetest)




#测试加入附加质量、附加科氏力、非线形阻尼（柯老师提供的参数）