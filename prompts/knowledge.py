

def creat_knowledge_visual_reasoning(en_flag):
    if en_flag:
        prompt = '''
Here is a short account of the key knowledge points and ways to slove problems in visual reasoning.

### **I. Key Knowledge Points: Rule Type Visual Reasoning**
#### 1. **Position Type (Pictures Made of Same Parts)**
- **Move Along**: Parts move on a flat space (way: up/down / left/right / across-corner / in a round way; number of steps: fixed, getting bigger, happening again and again; path: go through wall / turn back).
- **Turn Round**: Turning round a fixed point (way: with clock / against clock; angle: 45°, 90°, 180°, and so on).
- **Turn Over**: Turning over across a line (line across / line up and down, different from turning round: after turning over, the picture is like a looking-glass picture).

#### 2. **Style Type (Pictures Made of Parts That Are Like)**
- **Go Through All**: Parts come out again and again (go through all the picture, go through a small part, put in what is not there).
- **Add Take Away Same Different**:
 - Add / Take Away: Pictures put on top of each other or taking away parts that are on top of each other.
 - Take Same: Keep the parts that are the same (take same in the whole, take same in parts next to each other).
 - Take Different: Keep the parts that are not the same.
- **Black White Work**: Rules for putting black and white blocks on top of each other (like "black + white = black", be careful to keep it separate from moving along, often seen in nine-space boxes).

#### 3. **Quality Type (Pictures Made of Parts That Are Not The Same, Look at This First)**
- **Same On Both Sides** (Comes up often):
 - Line Same On Both Sides (number of lines, way, angle of turning, if it goes through point/line/surface).
 - Centre Same On Both Sides (is the same as the first picture after turning 180°).
 - Line + Centre Same On Both Sides (like "H" "O").
- **Straight Curved Quality**: All curved lines, all straight lines, curved and straight mixed (look at the whole first, then look inside/outside / up/down).
- **Open Closed Quality**: Closed pictures (with a break / without a break), part-closed, all open (be careful with pictures like those in everyday life, like "happy face" "key").

#### 4. **Number Type (Pictures Made of Parts That Are Not The Same, Look at This When Quality Has No Rule)**
- **Points**: Crossing points (total crossing points, curved and straight crossing points, touching points, end points).
- **Lines**:
 - Number of straight lines / curved lines (count separately, look for rules of getting bigger, or the rule of the number when one is taken from the other).
 - Number of pen movements (Key point):
 - **One pen movement**: A connected picture with 0 or 2 odd points (points where an odd number of lines come out).
 - **More than one pen movement**: Number of pen movements = number of odd points / 2 (number of odd points must be an even number).
- **Angles**: Right angles, sharp angles, flat angles (more detailed in later times: count the number of a certain kind of angle, like number of right angles).
- **Surfaces**: Number of closed areas (more detailed: shape of the area, size, black and white areas, number of same areas).
- **Units**:
 - Sort / Number of units (small separate pictures, like circles, three-sided shapes).
 - Number of parts (parts joined together are one part, often used for pictures like those in everyday life, like "leaf" "matches").

#### 5. **Special Rules**
- **Working Parts**: Marked points, arrows, small pictures (mark point: crossing points, lines, surfaces, angles; mark use: way, long/short, inside/outside).
- **Relation Between Pictures**:
 - Far from each other, touching (touching inside / touching outside), crossing (number of crossing lines / crossing points, curved/straight / long/short of crossing lines).
 - Inside (inside and outside structure, look at the quality of the inside picture).

### **II. Key Knowledge Points: Space Type Visual Reasoning**
#### 1. **Six-Side Box Folding (Will Be Asked)**
- **Opposite Sides**:
 - How to know: One space away in the same line or row, the two ends of a Z shape.
 - Quality: Opposite sides cannot be seen at the same time, and cannot be not seen at the same time.
- **Sides Next To Each Other**:
 - **Shared line**: The line where sides next to each other meet (length, look of it does not change after folding).
 - **Shared point**: The point where three sides meet (lines coming out from it do not change after folding).
 - **Arrow way**: Put an arrow on the only side that is not the same on both sides from the centre, see if the pictures up/down/left/right are the same.

#### 2. **Solid Joining**
- **Hollow and Bump Matching**: The part that goes in and the part that comes out are the same in shape and position (count the number of blocks first, then look at special shapes).

#### 3. **Cut Picture**
- **Cut Pictures of Common Solids**:
 - Six-side box: Three-sided shape (not right-angled), four-sided shape (square box, sloping box), five-sided shape, six-sided shape.
 - Round pipe: Circle (cut across), long round shape (cut slant), square box (cut up and down).
 - Round sharp top: Circle (cut across), long round shape (cut slant), three-sided shape (cut up and down through the top point).
- **Rule**: The cut is endless, the knife must cut straight to the end, it cannot turn.

#### 4. **Three View Pictures**
- **View Rules**: View from front (straight in front), view from left (left side), view from top (from above).
- **Small Points**: Broken lines mean lines you cannot see, be careful about the direction you are looking from and the outline of the picture.

### **III. Way to Do Questions and Steps to Solve**
#### 1. **Look Wide, Find the Type of Question**
- **Parts Are The Same**: Look first at Position Type (move along / turn round / turn over).
- **Parts Are Like**: Look first at Style Type (go through all, add take away same different, black white work).
- **Parts Are Not The Same**: Look first at Quality Type (same on both sides / straight curved / open closed), then Number Type (points / lines / angles / surfaces / units, try in the order "units surfaces angles lines points" because "units surfaces" are simple to see).
- **Special Rules**: Look at this when there are working parts or when a number of closed pictures are joined.

#### 2. **Look Close, Find the Special Rule**
- **Same On Both Sides**: First draw the line where it is the same on both sides, count the number, look at the way, find the rule (like the same-on-both-sides line turning 45°).
- **Number of Pen Movements**: When you see shapes like "sun" / "field" changed, pictures with many end points, circles crossing / touching, look first at the odd points.
- **Number of Surfaces**: The picture is cut up, closed surfaces are clear, look closely at the shape of the surfaces (like the number of three-sided surfaces).
- **Space Type**: Use the way of taking out wrong answers most of the time, opposite sides are taken out straight away, for sides next to each other use the shared line / point or arrow way to be certain.

#### 3. **Points Where Mistakes Are Easy and Skills**
- **Number Type Rules**: If there is no rule for the whole picture, think about looking at parts (like number of curved lines - number of straight lines = a fixed number), math work (like points + surfaces = lines), odd or even quality.
- **Black White Block Questions**: Part that is black (like 1/2 black), how they are joined (joined by point / joined by line), same on both sides, number of parts (are the black blocks joined together).
- **Cut Picture Traps**: Cutting a round sharp top slantwise will not make a straight line, cutting a six-side box slantwise will not make a right-angled three-sided shape.

Please keep in mind the knowledge points and ways to slove problems for visual reasoning that have been given, when answering questions after this:

'''
    else:
        prompt = f'''
下面总结了图形推理的核心知识点以及做题方法

### **一、核心知识点：规律类图形推理**
#### 1. **位置类（图形组成相同）**
- **平移**：元素在平面上移动（方向：上下/左右/对角线/环形；步数：恒定、递增、周期；路径：穿墙/折返）。  
- **旋转**：绕固定点转动（方向：顺/逆时针；角度：45°、90°、180°等）。  
- **翻转**：沿轴翻转（横轴/纵轴，与旋转区分：翻转后图形镜像对称）。  

#### 2. **样式类（图形组成相似）**
- **遍历**：元素重复出现（整体遍历、局部遍历，缺啥补啥）。  
- **加减同异**：  
  - 相加/相减：图形叠加或删除重叠部分。  
  - 求同：保留相同部分（整体求同、相邻求同）。  
  - 求异：保留不同部分。  
- **黑白运算**：黑白块叠加规则（如“黑+白=黑”，注意与位置平移区分，常出现在九宫格）。  

#### 3. **属性类（图形组成不同，优先考虑）**
- **对称性**（高频考点）：  
  - 轴对称（对称轴数量、方向、旋转角度、是否过点/线/面）。  
  - 中心对称（旋转180°后与原图重合）。  
  - 轴+中心对称（如“H”“O”）。  
- **曲直性**：全曲线、全直线、曲直混合（优先整体，再分内外/上下）。  
- **开闭性**：封闭图形（有缺口/无缺口）、半封闭、全开放（注意生活化图形，如“笑脸”“钥匙”）。  

#### 4. **数量类（图形组成不同，属性无规律时考虑）**
- **点**：交点（总交点、曲直交点、切点、端点）。  
- **线**：  
  - 直线/曲线数（分开数，关注递增、差值规律）。  
  - 笔画数（核心考点）：  
    - **一笔画**：连通图且奇点（引出奇数条线的点）数为0或2。  
    - **多笔画**：笔画数=奇点数/2（奇点数必为偶数）。  
- **角**：直角、锐角、钝角（近年细化：数某类角的数量，如直角数）。  
- **面**：封闭区域数（细化：面的形状、大小、黑白面、相同面数量）。  
- **素**：  
  - 元素种类/数量（独立小图形，如圆、三角形）。  
  - 部分数（连在一起为一部分，常用于生活化图形，如“树叶”“火柴”）。  

#### 5. **特殊规律**
- **功能元素**：标记点、箭头、小图形（标记位置：交点、线、面、角；标记作用：方向、长短、内外）。  
- **图形间关系**：  
  - 相离、相切（内切/外切）、相交（交线/交点数量、交线曲直/长短）。  
  - 包含（内外结构，关注内部图形属性）。  


### **二、核心知识点：空间类图形推理**
#### 1. **六面体折纸盒（必考题型）**
- **相对面**：  
  - 判定：同行/列隔一个、Z字形两端。  
  - 特性：相对面不能同时出现，也不能同时不出现。  
- **相邻面**：  
  - **公共边**：相邻面的交线（折叠前后长度、特征不变）。  
  - **公共点**：三个面相交的点（折叠前后引出线条不变）。  
  - **箭头法**：找唯一非中心对称面画箭头，判断上下左右图形是否一致。  

#### 2. **立体拼合**
- **凹凸对应**：凹进去的部分与凸出来的部分形状、位置一致（优先数块数，再看特殊形状）。  

#### 3. **截面图**
- **常见立体截面**：  
  - 正方体：三角形（非直角）、四边形（矩形、梯形）、五边形、六边形。  
  - 圆柱：圆（横切）、椭圆（斜切）、矩形（竖切）。  
  - 圆锥：圆（横切）、椭圆（斜切）、三角形（过顶点竖切）。  
- **原则**：截面无限大，刀需一刀切到底，不能拐弯。  

#### 4. **三视图**
- **投影规则**：主视图（正前方）、左视图（左侧）、俯视图（上方）。  
- **细节**：虚线表示不可见线条，注意视角方向和图形轮廓。  


### **三、做题方法与解题步骤**
#### 1. **宏观观察，确定题型范围**
- **组成相同**：优先位置类（平移/旋转/翻转）。  
- **组成相似**：优先样式类（遍历、加减同异、黑白运算）。  
- **组成不同**：先属性类（对称/曲直/开闭），再数量类（点/线/角/面/素，按“素面角线点”顺序尝试，因“素面”易观察）。  
- **特殊规律**：出现功能元素、多个封闭图形连接时考虑。  

#### 2. **微观分析，锁定具体规律**
- **对称性**：先画对称轴，数数量、看方向、找规律（如对称轴旋转45°）。  
- **笔画数**：出现“日/田”变形、多端点图、圆相交/相切，优先数奇点。  
- **面数量**：图形被分割、封闭面明显，细化考查面的形状（如三角形面数量）。  
- **空间类**：排除法为主，相对面直接排除，相邻面用公共边/点或箭头法验证。  

#### 3. **易错点与技巧**
- **数量类规律**：若整体无规律，考虑细分（如曲线数-直线数=常数）、运算（如点+面=线）、奇偶性。  
- **黑白块题型**：面积占比（如1/2阴影）、连接方式（点连接/线连接）、对称性、部分数（黑色块是否连在一起）。  
- **截面图陷阱**：圆锥斜切不会出直线，正方体斜切不会出直角三角形。    


请参考总结的图形推理的核心知识点以及做题方法回答接下来的问题：

'''
        
    return prompt



# visual reasoning, definition judgment, analogical reasoning, and logical judgment.
def creat_knowledge_definition_judgment(en_flag):
    if en_flag:
        prompt = '''
Here is a short account of the key knowledge points and ways to slove problems in knowledge definition.


### **I. Core Knowledge Points: Constituent Elements of Definition Judgment**  
The core of definition judgment questions lies in accurately understanding and applying the definitions provided in the questions. A complete definition typically includes the following core constituent elements, which need to be checked one by one when solving problems:  

1. **Subject**:  
   - The definition specifies who the doer of the action or the subject of the state is.  
   - This may be individuals with specific identities (e.g., civil servants, minors), specific organizations (e.g., legal entities, government agencies), groups with certain characteristics (e.g., consumers, taxpayers), or general references (e.g., anyone).  
   - **Key**: Determine whether the subject in the option falls within the scope defined by the definition.  

2. **Object/Target**:  
   - The definition specifies the target of the action or the involved entity.  
   - This may be concrete items (e.g., public property), abstract concepts (e.g., information, reputation), specific relationships (e.g., contractual relationships), or specific groups (e.g., vulnerable populations).  
   - **Key**: Determine whether the action in the option acts on the object specified by the definition.  

3. **Action/State/Property**:  
   - The core content of the definition, describing what is specifically done, what state is occupied, or what properties are possessed.  
   - This may include specific actions (e.g., theft, rescue), psychological activities (e.g., intent, negligence), processes (e.g., decision-making processes), result states (e.g., loss, validity), or attribute characteristics (e.g., suddenness, contingency).  
   - **Key**: Determine whether the main action or state described in the option matches the core description of the definition.  

4. **Conditions/Situations/Methods**:  
   - Definitions often specify the specific background, preconditions, or means by which the action occurs.  
   - Examples: "during working hours," "without permission," "by violent means," "for public interest."  
   - **Key**: Determine whether the situations, conditions, or methods described in the option meet all the restrictions in the definition.  

5. **Purpose/Cause/Result**:  
   - Definitions sometimes specify the purpose of the action, the triggering cause, or the necessary outcome.  
   - Examples: "for profit," "due to force majeure," "leading to serious consequences," "aimed at improving efficiency."  
   - **Key**: Determine whether the motivation, cause, or consequence of the action in the option complies with the definition’s requirements.  

6. **Qualifiers/Keywords**:  
   - Definitions often include words that play a critical limiting role, such as "must," "main," "only," "or," "and," "excluding," "at least," "intentional," "negligent," etc.  
   - **Key**: Accurately understand the logical meanings and scopes of these words, as they often serve as the key to distinguishing between options.  


### **II. Problem-Solving Methods and Steps**  

1. **Read the Definition Carefully and Deconstruct Core Elements**:  
   - **Step 1**: Read the definition thoroughly to grasp its overall meaning.  
   - **Step 2**: Read slowly and "deconstruct" the definition to identify core constituent elements such as [Subject], [Object], [Action/State], [Conditions/Situations], and [Purpose/Result].  
   - **Step 3**: Pay special attention to [Qualifiers/Keywords], marking them with a pen or memorizing them mentally to clarify the definition’s boundaries and core requirements. This can be simplified as "who, to whom/what, under what circumstances, in what way, did what, for what purpose/led to what result."  

2. **Analyze Options One by One and Compare with Definition Elements**:  
   - **Step 4**: Read the first option and extract its key information (also decomposable by elements such as subject, action, conditions, etc.).  
   - **Step 5**: Strictly and systematically compare the option’s information with the definition’s core elements. Check whether the option fully satisfies all necessary conditions of the definition:  
     - Does the subject match?  
     - Is the action/state consistent?  
     - Are the conditions/situations met?  
     - Is the purpose/result achieved?  
     - Does it violate any exclusion clauses?  
     - Are the keyword restrictions observed?  

3. **Filter, Judge, Eliminate, and Select**:  
   - **Step 6**:  
     - **For "belongs to" questions**: If an option fully meets all elements of the definition, it is likely the correct answer; if any **necessary** element does not match, **eliminate it directly**.  
     - **For "does not belong to" questions**: Look for the **single** option that does not fully meet the definition’s elements. Typically, the other three options will perfectly fit the definition.  
   - **Step 7**: Repeat Steps 4–6 for the remaining options. The elimination method usually helps lock in the answer quickly.  

4. **Compare and Choose the Best (for Ambiguous Options)**:  
   - **Step 8**: If multiple options seem to fit or not fit (rare), return to the definition, read the keywords and implicit logic carefully, and compare which option is closer to or further from the definition’s **core characteristics** or **essential provisions**. Choose the one that best matches or mismatches the definition.  


### **III. Common Pitfalls and Tips**  

1. **Subjective Assumptions, Deviating from the Definition**: The most common mistake is judging based on life experience or prior knowledge instead of strictly adhering to the **specific definition given in the question**. Always take the definition as the sole criterion.  
2. **Overlooking Keywords**: Failing to notice qualifiers like "must," "main," or "intentional," leading to misinterpretations of the definition’s scope.  
3. **Missing Elements**: Selecting an option that satisfies some but not all **necessary** elements of the definition. Ensure all **hard rules** are met.  
4. **Conceptual Confusion**: The option describes a situation similar to the definition’s concept but essentially different (e.g., "justifiable defense" vs. "excessive defense").  
5. **Pay Attention to "Or" vs. "And"**: Clarify whether the definition uses "or" (satisfying one condition is enough) or "and" (all conditions must be met simultaneously).  
6. **Positive/Negative Question Formats**: Check carefully whether the question asks "belongs to" or "does not belong to" the definition to avoid choosing the opposite.  
7. **"Word-Picking" Technique**: Definition judgment is essentially about information matching and logical judgment. Sometimes, it requires meticulous comparison of subtle wording differences between options and the definition.  
8. **Core Simplification Method**: For complex definitions, paraphrase the core meaning in your own words ("one-sentence summary") to grasp the essence before evaluating options.  
9. **Element Checklist Method**: Mentally or on paper list the definition’s key elements and check each option against them with ticks or crosses for clarity.
Please keep in mind the knowledge points and ways to slove problems for knowledge definition that have been given, when answering questions after this:

'''
    else:

        prompt = f'''
下面总结了定义判断的核心知识点以及做题方法：

### **一、核心知识点：定义判断的构成要素**

定义判断题型的核心在于精确理解和应用题目给出的定义。一个完整的定义通常包含以下几个核心构成要素，解题时需要逐一核对：

1.  **主体**：
    * 定义规定了行为或状态的发出者是谁。
    * 可能是特定身份的人（如公务员、未成年人）、特定组织（如法人、政府机关）、具有某种特征的群体（如消费者、纳税人）或泛指（如任何人）。
    * **关键**：判断选项中的主体是否符合定义限定的范围。

2.  **客体/对象**：
    * 定义规定了行为所指向的对象或涉及的事物。
    * 可能是具体物品（如公共财产）、抽象概念（如信息、名誉）、特定关系（如合同关系）或特定群体（如弱势群体）。
    * **关键**：判断选项中的行为是否作用于定义所规定的客体上。

3.  **行为/状态/性质**：
    * 定义的核心内容，描述了具体做了什么、处于什么状态或具备什么性质。
    * 可能是具体的动作（如盗窃、救助）、心理活动（如故意、过失）、过程（如决策过程）、结果状态（如亏损、有效）或属性特征（如突发性、偶然性）。
    * **关键**：判断选项描述的主要行为或状态是否与定义的核心描述一致。

4.  **条件/情境/方式**：
    * 定义常常限定行为发生的特定背景、前提条件或方式手段。
    * 例如：“在工作时间”、“未经许可”、“通过暴力手段”、“为了公共利益”。
    * **关键**：判断选项描述的情境、条件或方式是否满足定义中的所有限制。

5.  **目的/原因/结果**：
    * 定义有时会规定行为的目的、引发原因或必须达到的结果。
    * 例如：“以营利为目的”、“因不可抗力”、“导致严重后果”、“旨在提高效率”。
    * **关键**：判断选项中行为的动机、原因或产生的后果是否符合定义的要求。

6.  **限定词/关键词**：
    * 定义中常包含起关键限定作用的词语，如“必须”、“主要”、“唯一”、“或者”、“并且”、“不包括”、“至少”、“故意”、“过失”等。
    * **关键**：准确理解这些词语的逻辑含义和限制范围，它们往往是区分选项的关键。

### **二、做题方法与解题步骤**

1.  **仔细阅读定义，拆解核心要素**：
    * **第一步**：通读定义，理解其整体含义。
    * **第二步**：慢读并“拆解”定义，识别出上述的【主体】、【客体】、【行为/状态】、【条件/情境】、【目的/结果】等核心构成要件。
    * **第三步**：特别注意【限定词/关键词】，用笔标记或心中默记，明确定义的边界和核心要求。可以简化为“谁，对谁/什么，在什么情况下，以什么方式，做了什么，目的是什么/导致什么结果”。

2.  **逐一分析选项，与定义要素比对**：
    * **第四步**：阅读第一个选项，提取其描述的关键信息（同样可以按主体、行为、条件等要素来分解）。
    * **第五步**：将选项信息与定义的核心要素进行【严格】、【逐一】比对。检查选项是否【完全满足】定义中的【所有】必要条件。
        * 主体是否符合？
        * 行为/状态是否一致？
        * 条件/情境是否满足？
        * 目的/结果是否达到？
        * 是否触犯了排除性条款？
        * 关键词的限制是否遵守？

3.  **筛选判断，排除与选择**：
    * **第六步**：
        * **对于“属于”类问题**：如果选项完全符合定义的所有要素，则可能是正确答案；如果任何一个【必要】要素不符，则【直接排除】。
        * **对于“不属于”类问题**：寻找那个【唯一】不完全符合定义要素的选项。通常其他三个选项会完美契合定义。
    * **第七步**：重复步骤四至六，分析其余选项。通常运用排除法可以快速锁定答案。

4.  **比较择优（若有模糊选项）**：
    * **第八步**：如果遇到多个选项看似都符合或都不符合的情况（较少见），需要【再次】回到定义，精读关键词和隐含逻辑，比较哪个选项与定义的【核心特征】或【最本质规定】更贴近或偏离最远。选择最符合或最不符合的那一个。

### **三、易错点与技巧**

1.  **主观臆断，脱离定义**：最常见的错误是凭生活经验或已有知识进行判断，而不是严格依据【题目给出的特定定义】。务必以定义为唯一标准。
2.  **忽略关键词**：未能注意到“必须”、“主要”、“故意”等限定词，导致对定义的范围理解错误。
3.  **要素缺失或不全**：选项满足了定义的部分要素，但未能满足全部【必要】要素，被误选。要确保所有【硬性规定】都满足。
4.  **概念混淆**：选项描述的情况与定义涉及的概念相似，但实质不同（如“正当防卫”与“防卫过当”）。
5.  **注意“或”与“且”**：看清定义中是用“或”连接条件（满足其一即可）还是用“且”/“并”（必须同时满足）。
6.  **肯定/否定提问方式**：看清楚题目问的是“属于”还是“不属于”该定义，避免选反。
7.  **“抠字眼”技巧**：定义判断本质上是信息匹配和逻辑判断，有时需要细致地“抠字眼”，对比选项和定义在表述上的细微差别。
8.  **简化核心法**：对于复杂的定义，尝试用自己的话转述其核心意思（“一句话概括”），抓住本质，再去看选项会更清晰。
9.  **要素核对表法**：心里或纸上列出定义的几个关键要素，逐个核对选项是否满足，打勾或打叉，一目了然。


请参考总结的定义判断的核心知识点以及做题方法回答接下来的问题：

        '''


        
    return prompt



def creat_knowledge_analogical_reasoning(en_flag):
    if en_flag:
        prompt = '''
Here is a short account of the key knowledge points and ways to slove problems in analogical reasoning.

### **I. Core Knowledge Points: Foundations of Analogical Reasoning**  
#### 1. **Question Type Classification**  
- **Two-Word Type**: A∶B (e.g., "Apple∶Fruit"), directly analyze the relationship between the two terms.  
- **Three-Word Type**: A∶B∶C (e.g., "Teacher∶Classroom∶Teaching"), require analyzing pairwise relationships or overall connections.  
- **Fill-in-the-Blank Type**: A is to ( ) as ( ) is to B (e.g., "( ) is to Mobile Phone as Communication is to ( )"), which requires substituting options to verify consistent logic before and after.  

#### 2. **Logical Relationships (High-Frequency Test Points)**  
##### (1) **Extensional Relationships (Relationships Between Conceptual Scopes of Terms)**  
- **Total Identity Relationship**: The concepts of the two terms completely overlap (e.g., "Potato∶Potato" [same term in different names], "Beijing∶Capital of China").  
- **Parallel Relationship**:  
  - **Contradictory Relationship**: Non-exclusive and exhaustive (e.g., "Life∶Death", "Male∶Female"—no third category exists).  
  - **Oppositional Relationship**: Belong to the same category but have intermediate terms (e.g., "Red∶White", "Apple∶Banana"—other colors/fruits exist).  
- **Inclusive Relationship**:  
  - **Subordinate Relationship**: A is a type of B (e.g., "Sparrow∶Bird"—sparrow belongs to the bird category).  
  - **Compositional Relationship**: A is a component of B (e.g., "Wheel∶Car"—wheel is a part of a car).  
- **Intersectional Relationship**: Concepts partially overlap (e.g., "Party Member∶College Student"—some party members are college students, and vice versa).  

##### (2) **Intensional Relationships (Internal Connections Between Terms)**  
- **Correspondence Relationship** (core test point, requires flexible accumulation):  
  - **Functional Correspondence**: Object and its function (e.g., "Pen∶Writing", "Streetlight∶Illuminating").  
  - **Causal Correspondence**: Cause and effect (e.g., "Rain∶Wet Ground", "Effort∶Success").  
  - **Temporal Sequence**: Order of actions (e.g., "Buy Ticket∶Board Vehicle", "Get Up∶Wash Up"—note if the subject is the same).  
  - **Raw Material Correspondence**: Finished product and its raw material (e.g., "Wood∶Furniture", "Flour∶Steamed Bun"—distinguish physical/chemical changes).  
  - **Attribute Correspondence**: Object and its characteristics (e.g., "Salt∶Salty", "Flower∶Fragrant"—divided into necessary and contingent attributes).  
  - **Location Correspondence**: Action and its occurrence place (e.g., "Doctor∶Hospital", "Class∶Classroom").  
  - **General Knowledge Correspondence**: Literary, historical, geographical, etc. (e.g., "Lu Xun∶*The Scream*", "Beijing∶China").  

##### (3) **Semantic Relationships**  
- **Synonym Relationship**: Similar meanings (e.g., "Happy∶Joyful", "Serious∶Meticulous").  
- **Antonym Relationship**: Opposite meanings (e.g., "Tall∶Short", "Success∶Failure").  
- **Metaphorical and Symbolic Meaning**: Extended meanings through metaphor (e.g., "Moon∶Longing", "Dove∶Peace").  

##### (4) **Grammatical Relationships**  
- **Subject-Predicate Relationship**: Subject + predicate (e.g., "Student∶Study", "Actor∶Perform").  
- **Verb-Object Relationship**: Verb + object (e.g., "Play Basketball", "Kick Football").  
- **Modifier-Center Relationship**: Modifier + central word (e.g., "Beautiful∶Flower", "Rapid∶Run"—connected by adjective or verb).  
- **Parallel Structure**: Consistent parts of speech and structure (e.g., "Sing∶Dance", "Joy and Sorrow∶Separation and Reunion").  

#### 3. **Secondary Analysis (Used When Options Are Difficult to Differentiate)**  
- **Part of Speech**: Noun, verb, adjective (e.g., "Achievement∶Result∶Consequence"—all nouns, but different emotional tones).  
- **Emotional Tone**: Positive, negative, neutral (e.g., "Decisive∶Arbitrary"—the former is positive, the latter negative).  
- **Degree Progression**: Gradation of intensity in synonyms (e.g., "Like∶Love", "Cold∶Freezing").  
- **Necessity vs. Contingency**: Whether an attribute necessarily exists (e.g., "Metal∶Conductive" is necessary; "Flower∶Red" is contingent).  
- **Consistency of Subject**: Whether the doer of the action is the same (e.g., "Buy Ticket∶Board Vehicle" has the same subject; "Teach∶Attend Class" has different subjects).  
- **Nomenclature Method**: Naming based on shape, function, person, etc. (e.g., "Thermos Cup∶Heat Preservation [function]", "Lily of the Valley∶Shaped like a lily bell").  


### **II. Problem-Solving Methods and Steps**  
#### 1. **Problem-Solving Steps: "First Horizontal, Then Vertical; First Primary, Then Secondary"**  
- **Step 1: Analyze Horizontal Relationships in the Question Stem**  
  - Prioritize judging logical (extensional, intensional), semantic, or grammatical relationships; eliminate obviously inconsistent options.  
  - Example: Question stem "Sparrow∶Bird" (subordinate relationship). If an option is "Tomato∶Vegetable" (subordinate), keep it; if "Leaf∶Tree" (compositional), eliminate it.  
- **Step 2: Vertically Compare Remaining Options**  
  - When horizontal relationships are consistent, compare whether the part of speech, emotional tone, category (e.g., natural/artificial), etc., of the options are closer to the question stem.  
  - Example: Question stem "White Vinegar∶Disinfection" (functional correspondence, secondary function). The option "Gasoline∶Stain Removal" (secondary function) is more appropriate than "Water Heater∶Heating" (primary function).  
- **Step 3: Use Secondary Analysis to Lock the Answer**  
  - If multiple options still fit, further filter using secondary analysis (e.g., necessary vs. contingent attributes, subject consistency).  

#### 2. **High-Frequency Relationship Problem-Solving Techniques**  
##### (1) **Distinguishing Subordinate vs. Compositional Relationships**  
- Use the "is" test: If "A is B" holds, it is subordinate (e.g., "Apple is a fruit"). If not, it is compositional (e.g., "Screen is a part of a phone" ≠ "Screen is a phone").  

##### (2) **Contradictory vs. Oppositional in Parallel Relationships**  
- Check for a "third party": None indicates contradictory (e.g., "On-Off"—no middle state), while existence indicates oppositional (e.g., "Colors"—red, yellow, blue, etc. exist).  

##### (3) **Combining Temporal Sequence and Causal Relationships**  
- For multiple-action questions, prioritize temporal order; if a causal relationship exists (e.g., "Fall Ill∶Take Medicine"), further judge if the causal direction is consistent.  

##### (4) **Idiom-Based Questions**  
- First analyze the structure by splitting the idiom: e.g., "Carve the Boat to Seek the Sword" (means-end relationship), "Lips Gone, Teeth Cold" (causal relationship).  
- Then examine semantics: synonyms (e.g., "Quench Thirst by Watching Plums∶Relieve Hunger by Drawing Bread") or antonyms (e.g., "Live and Work in Peace∶Wander Destitute").  

#### 3. **Common Pitfalls and Tips**  
- **Pitfall 1: Conceptual Shift**  
  - Example: "Eye∶Glasses" (auxiliary tool) vs. "Tooth∶Toothbrush" (cleaning tool)—pay attention to specific functional correspondence.  
- **Pitfall 2: Ignoring the Order of Secondary Analysis**  
  - Prioritize primary relationships (e.g., logical relationships) before secondary analysis (e.g., emotional tone); avoid direct vertical comparison first.  
- **Pitfall 3: Confusing Causal and Conditional Relationships**  
  - Causality is fact-based (e.g., "Rain∶Wet Ground"), while conditionality is hypothesis-based (e.g., "x>1∶x²>1").  
- **Pitfall 4: Neglecting Sequential Relationships**  
  - Pay attention to temporal, alphabetical, or numerical order (e.g., "Spring Planting∶Summer Growth∶Autumn Harvest").

Please keep in mind the knowledge points and ways to slove problems for analogical reasoning that have been given, when answering questions after this:

'''
    else:
        prompt = f'''

下面总结了类比推理的核心知识点以及做题方法

### **一、核心知识点：类比推理基础**  
#### 1. **题型分类**  
- **两词型**：A∶B（如“苹果∶水果”），直接分析两者关系。  
- **三词型**：A∶B∶C（如“教师∶教室∶教学”），需两两找关系或整体关联。  
- **填空型**：A对于（ ）相当于（ ）对于B（如“（ ）对于手机相当于交流对于（ ）”），需代入选项验证前后逻辑一致。  

#### 2. **逻辑关系（高频考点）**  
##### （1）**外延关系（词项概念范围间的关系）**  
- **全同关系**：两词概念完全重合（如“土豆∶马铃薯”“北京∶中国首都”）。  
- **并列关系**：  
  - **矛盾关系**：非此即彼（如“生∶死”“男∶女”，无第三种情况）。  
  - **反对关系**：同属一类但存在中间项（如“红∶白”“苹果∶香蕉”，有其他颜色/水果）。  
- **包含关系**：  
  - **种属关系**：A是B的一种（如“麻雀∶鸟”，麻雀属于鸟类）。  
  - **组成关系**：A是B的组成部分（如“车轮∶汽车”，车轮是汽车的一部分）。  
- **交叉关系**：概念有部分重叠（如“党员∶大学生”，有的党员是大学生，有的不是）。  

##### （2）**内涵关系（词项内在联系）**  
- **对应关系**（核心考点，需灵活积累）：  
  - **功能对应**：事物与其功能（如“钢笔∶书写”“路灯∶照明”）。  
  - **因果对应**：原因与结果（如“下雨∶地湿”“努力∶成功”）。  
  - **时间顺序**：动作先后（如“购票∶乘车”“起床∶洗漱”，注意主体是否一致）。  
  - **原材料对应**：成品与原材料（如“木材∶家具”“面粉∶馒头”，区分物理/化学变化）。  
  - **属性对应**：事物与其特性（如“盐∶咸”“花∶香”，分为必然属性和或然属性）。  
  - **场所对应**：行为与其发生场所（如“医生∶医院”“上课∶教室”）。  
  - **常识对应**：文学、历史、地理等（如“鲁迅∶《呐喊》”“北京∶中国”）。  

##### （3）**语义关系**  
- **近义关系**：词语含义相近（如“高兴∶喜悦”“认真∶细致”）。  
- **反义关系**：词语含义相反（如“高∶矮”“成功∶失败”）。  
- **比喻象征义**：通过比喻产生的引申义（如“月亮∶思念”“鸽子∶和平”）。  

##### （4）**语法关系**  
- **主谓关系**：主语+谓语（如“学生∶学习”“演员∶表演”）。  
- **动宾关系**：动词+宾语（如“打篮球”“踢足球”）。  
- **偏正关系**：修饰词+中心词（如“美丽∶花朵”“快速∶奔跑”，用“的/地”连接）。  
- **并列结构**：词性、结构一致（如“唱歌∶跳舞”“悲欢∶离合”）。  

#### 3. **二级辨析（选项难分时使用）**  
- **词性**：名词、动词、形容词（如“成果∶结果∶后果”，均为名词，但感情色彩不同）。  
- **感情色彩**：褒义、贬义、中性（如“果断∶武断”，前者褒义，后者贬义）。  
- **程度递进**：近义词的轻重程度（如“喜欢∶热爱”“寒冷∶严寒”）。  
- **必然与或然**：属性是否必然存在（如“金属∶导电”为必然，“花朵∶红色”为或然）。  
- **主体一致**：行为的发出者是否相同（如“购票∶乘车”主体一致，“授课∶听课”主体不同）。  
- **命名方式**：根据形状、功能、人物等命名（如“保温杯∶保温（功能）”“马蹄莲∶形状像马蹄”）。  


### **二、做题方法与解题步骤**  
#### 1. **解题步骤：“先横后纵，先一级后二级”**  
- **第一步：横向分析题干关系**  
  - 优先判断逻辑关系（外延、内涵）、语义关系或语法关系，排除明显不符的选项。  
  - 例：题干“麻雀∶鸟”（种属关系），选项若为“番茄∶蔬菜”（种属）则保留，若为“树叶∶树”（组成）则排除。  
- **第二步：纵向对比剩余选项**  
  - 当横向关系一致时，对比选项与题干的词性、感情色彩、范畴（如自然物/人造物）等是否更贴近。  
  - 例：题干“白醋∶消毒”（功能对应，且为次要功能），选项“汽油∶去渍”（次要功能）比“热水器∶加热”（主要功能）更合适。  
- **第三步：二级辨析锁定答案**  
  - 若仍有多个选项符合，结合二级辨析（如必然属性vs或然属性、主体是否一致）进一步筛选。  

#### 2. **高频关系解题技巧**  
##### （1）**区分种属与组成关系**  
- 用“是”造句：能直接说“A是B”为种属（如“苹果是水果”）；不能则为组成（如“屏幕是手机的组成部分”≠“屏幕是手机”）。  

##### （2）**并列关系的矛盾与反对**  
- 看是否有“第三者”：无即为矛盾（如“开关”非开即关），有即为反对（如“颜色”有红、黄、蓝等）。  

##### （3）**时间顺序与因果关系的结合**  
- 多个动作题优先看时间先后，若存在因果关系（如“生病∶吃药”），需进一步判断因果方向是否一致。  

##### （4）**成语类题目**  
- 先拆词分析结构：如“刻舟求剑”（方式目的）、“唇亡齿寒”（因果关系）。  
- 再看语义：近义（如“望梅止渴∶画饼充饥”）或反义（如“安居乐业∶颠沛流离”）。  

#### 3. **易错点与技巧**  
- **陷阱一：偷换概念**  
  - 例：“眼睛∶眼镜”（辅助工具）vs“牙齿∶牙刷”（清洁工具），需注意功能的具体对应。  
- **陷阱二：忽略二级辨析顺序**  
  - 优先判断一级关系（如逻辑关系），再考虑二级辨析（如感情色彩），避免直接纵向对比。  
- **陷阱三：因果与条件关系混淆**  
  - 因果基于事实（如“下雨：地湿”），条件基于假设（如“x>1：x²>1”）。  
- **陷阱四：顺序关系忽视**  
  - 注意时间、字母、数字顺序（如“春种：夏长：秋收”）。   

请参考总结的类比推理的核心知识点以及做题方法回答接下来的问题：
'''


        
    return prompt


def creat_knowledge_logical_judgment(en_flag):
    if en_flag:
        prompt = '''
Here is a short account of the key knowledge points and ways to slove problems in logical judgment.


### I. Core Knowledge Points  

#### (1) Necessary Reasoning  
1. **Translational Reasoning**  
   - **Question Type Judgment**: The question stem or options contain typical logical connectives such as "if...then...", "only if...".  
   - **Answering Techniques**: Translate first, then reason. Translate sentences with logical connectives in the question stem into relationships denoted by arrows (→).  
   - **Translation Principles**:  
     - Place the necessary condition after the arrow. For example, "A is a necessary condition for B" is translated as "B→A".  
     - "...unless... = unless...otherwise... = unless...otherwise not..." For example, "Unless A, otherwise not B" is translated as "B→A".  
   - **Reasoning Principles**:  
     - **Contrapositive Equivalence**: "Antecedent→Consequent" is equivalent to "¬Consequent→¬Antecedent". Neither "denying the antecedent" nor "affirming the consequent" can yield a definite conclusion.  
     - **Transitive Law**: "1→2, 2→3" is equivalent to "1→3". The transitive law cannot be applied if the same element appears only on the antecedent or consequent side of all arrows.  
   - **AND and OR Relationships**:  
     - **AND Relationship**: Indicates a conjunction (and, both...and..., etc.).  

2. **Naive Logic**  
   - **Question Type Characteristics**: The question stem provides conditions that require reasoning to derive a conclusion.  
   - **Problem-Solving Methods**:  
     - Use the substitution method when option information is sufficient.  
     - In more difficult questions, the answer is often among the earlier options.  

#### (2) Probabilistic Reasoning  
1. **Weakening Arguments**  
   - **Weakening the Thesis**: Directly challenge the thesis by proposing an opposite view or counterexample.  
   - **Weakening the Evidence**: Point out flaws or inadequacies in the evidence.  
   - **Breaking the Link**: Disrupt the logical connection between the thesis and the evidence.  
   - **Denying the Premise**: Negate the necessary conditions for the thesis to hold.  
   - **Causal Inversion**: In causal weakening questions, causal inversion is generally the answer.  
   - **Alternative Cause**: Weakening in control experiments typically involves identifying an alternative cause.  

2. **Strengthening Arguments**  
   - **Strengthening the Thesis**: Explicitly affirm the thesis or provide consistent information.  
   - **Strengthening the Evidence**: Provide more robust support for the thesis.  
   - **Establishing a Link**: Build a logical "bridge" between the thesis and the evidence.  
   - **Supplementing Premises**: Identify indispensable conditions for the thesis to hold.  
   - **Elimination of Alternative Causes**: Strengthening in control experiments typically involves eliminating alternative causes.  

### II. Problem-Solving Methods and Steps  

#### (1) Macro Observation to Determine the Question Type  
1. **Translational Reasoning**: Prioritize translational reasoning when logical connectives are present.  
2. **Naive Logic**: Use naive logic when the question stem contains numerous complex conditions.  
3. **Probabilistic Reasoning**: Identify whether it is a weakening or strengthening question based on the presence of a thesis and evidence in the question stem.  

#### (2) Micro Analysis to Lock in Specific Rules  
1. **Translational Reasoning**: Translate the question stem first, then analyze options using reasoning rules.  
2. **Naive Logic**: Reason step-by-step based on the given conditions; use the substitution method when necessary.  
3. **Probabilistic Reasoning**:  
   - **Weakening Arguments**: Prioritize direct negation of the conclusion or causal inversion.  
   - **Strengthening Arguments**: Prioritize supplementing evidence or establishing logical links.  

### III. Common Pitfalls and Tips  
1. **Translational Reasoning**: Remember that "denying the antecedent" and "affirming the consequent" cannot yield definite conclusions.  
2. **Probabilistic Reasoning**:  
   - In weakening, direct negation of the conclusion and causal inversion are highly effective.  
   - In strengthening, supplementing evidence and eliminating alternative causes are strongly supportive.  
3. **Control Experiments**: Weakening typically involves alternative causes; strengthening typically involves eliminating alternative causes.  
4. **Premise Assumptions**: Options addressing the "jump" between premises and conclusions in the argument are generally the answer.

Please keep in mind the knowledge points and ways to slove problems for logical judgment that have been given, when answering questions after this:

'''
    else:
        prompt = f'''
下面总结了逻辑判断的核心知识点以及做题方法

### 一、核心知识点

#### （一）必然性推理
1. **翻译推理**
   - **判断题型**：题干或选项出现“如果...那么...，只有...才...”等典型逻辑关系词。
   - **答题技巧**：先翻译，后推理。将题干中逻辑关联词所在句子翻译成用箭头推出的关系。
   - **翻译原则**：
     - 谁是必要条件，谁放在箭头后面。如“A是B的必要条件”翻译为“B→A”。
     - “...除非... = 除非...否则... = 除非...否则不（不）...”，如“除非A，否则不B”翻译为“B→A”。
   - **推理原则**：
     - 逆否等价：“前→后”等价于“否后→否前”，“否前”和“肯后”均推不出确定的结论。
     - 传递规律：“1→2，2→3”等价于“1→3”，相同要素如果都在箭头前或后，不能使用传递规律。
   - **且与或**：
     - “且”关系：并列关系（且、并且、和、及、与、同、都、既...又...）。

2. **朴素逻辑**
   - **题型特点**：题干给出一些条件，需要通过推理得出结论。
   - **解题方法**：
     - 选项信息充分时，使用代入法。
     - 题目越难，答案越靠前。

#### （二）可能性推理
1. **削弱论证**
   - **削弱论点**：直接对论点发起挑战，提出与之相反的观点或反例。
   - **削弱论据**：指出论据存在的漏洞或不足之处。
   - **切断联系**：破坏论点和论据之间的逻辑关联。
   - **否定前提**：对论点成立的必要条件进行否定。
   - **因果倒置**：在因果论证的削弱题中，因果倒置基本为答案。
   - **另有他因**：对比实验的削弱一般为另有他因。

2. **加强论证**
   - **加强论点**：明确肯定论点或者提供与之一致的信息。
   - **加强论据**：为论点提供更有力的支撑。
   - **建立联系**：在论点和论据之间搭建逻辑的“桥梁”。
   - **补充前提**：找到论点成立必不可少的条件。
   - **排除他因**：对比实验的加强一般为排除他因。

### 二、做题方法与解题步骤

#### （一）宏观观察，确定题型范围
1. **翻译推理**：看到关联词，优先考虑翻译推理。
2. **朴素逻辑**：题干条件较多且复杂，考虑朴素逻辑。
3. **可能性推理**：题干中有论点和论据，判断是削弱还是加强。

#### （二）微观分析，锁定具体规律
1. **翻译推理**：先翻译题干，再根据推理规则分析选项。
2. **朴素逻辑**：根据题干条件逐步推理，必要时使用代入法。
3. **可能性推理**：
   - **削弱论证**：优先考虑直接否定结论或因果倒置。
   - **加强论证**：优先考虑补充论据或建立联系。

### 三、易错点与技巧
1. **翻译推理**：注意“否前”和“肯后”均推不出确定的结论。
2. **可能性推理**：
   - 削弱中，直接否定结论、因果倒置的削弱力度很强。
   - 加强中，补充论据、排除他因的加强力度较强。
3. **对比实验**：削弱一般为另有他因，加强一般为排除他因。
4. **前提假设**：涉及前提和结论中的跳跃概念的选项基本为答案。


请参考总结的逻辑判断的核心知识点以及做题方法回答接下来的问题：

'''
        
    return prompt


