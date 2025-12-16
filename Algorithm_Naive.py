# algorithm1.py
# استيراد المكتبات اللازمة (رغم أننا قد لا نحتاجها كلها هنا، لكن احتياطاً)
import sys

# زيادة حد التكرار (Recursion Limit) لتجنب توقف البرنامج عند استخدام DFS مع بيانات كبيرة
sys.setrecursionlimit(20000)

# تعريف دالة البحث في العمق (DFS) للكشف عن وجود مسار بين نقطتين
def has_path_dfs(adj, current, target, visited):
    # الحالة الأساسية: إذا وصلنا للنقطة المطلوبة، نرجع True (يوجد مسار)
    if current == target:
        return True
    
    # إضافة النقطة الحالية إلى قائمة "تمت زيارتها" لتجنب الدوران اللانهائي
    visited.add(current)
    
    # المرور على جميع جيران النقطة الحالية
    for neighbor in adj.get(current, []):
        # إذا لم تتم زيارة الجار من قبل
        if neighbor not in visited:
            # نستدعي الدالة نفسها (Recursion) للبحث انطلاقاً من الجار
            if has_path_dfs(adj, neighbor, target, visited):
                return True # وجدنا مساراً
    
    # إذا انتهى البحث ولم نجد شيراً
    return False

# الدالة الرئيسية لتنفيذ الحل الساذج (Naive MST)
def solve_naive(num_buildings, all_edges):
    # ترتيب جميع الكابلات (الحواف) تصاعدياً حسب الوزن (التكلفة) - خطوة أساسية لـ Kruskal
    sorted_edges = sorted(all_edges, key=lambda x: x[2])
    
    # قائمة لتخزين الكابلات التي سيتم اختيارها في الحل النهائي
    mst_edges = []
    
    # متغير لتخزين التكلفة الإجمالية للكابلات المختارة
    mst_cost = 0
    
    # إنشاء قاموس لتمثيل الشبكة (Adjacency List) لتخزين التوصيلات الحالية
    adj = {i: [] for i in range(num_buildings)}
    
    # عداد للكابلات التي تم تركيبها
    count = 0
    
    # المرور على كل الكابلات المتاحة بالترتيب (من الأرخص للأغلى)
    for u, v, w in sorted_edges:
        # شرط التوقف: إذا وصلنا لعدد كابلات يساوي (عدد المباني - 1)، فقد اكتملت الشجرة
        if count == num_buildings - 1:
            break
        
        # إنشاء مجموعة فارغة لتخزين النقاط التي زارها DFS في هذه الدورة
        visited = set()
        
        # --- الجزء الساذج (Naive Part) ---
        # نستخدم DFS للتحقق: هل المبنيان (u) و (v) متصلان بالفعل؟
        # إذا كانا متصلين، فإضافة هذا الكابل ستصنع دائرة (Cycle)، وهذا ممنوع.
        if not has_path_dfs(adj, u, v, visited):
            # إذا لم يكونا متصلين (False)، نقوم باختيار هذا الكابل
            mst_edges.append((u, v, w))
            
            # نضيف التكلفة للمجموع الكلي
            mst_cost += w
            
            # نحدث الشبكة بإضافة التوصيلة في الاتجاهين (لأن الشبكة غير موجهة)
            adj[u].append(v)
            adj[v].append(u)
            
            # نزيد العداد 1
            count += 1
            
    # إرجاع التكلفة النهائية وقائمة الكابلات المختارة
    return mst_cost, mst_edges