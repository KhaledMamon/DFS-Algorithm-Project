# algorithm2.py

# تعريف كلاس (Union-Find) وهو هيكل بيانات ذكي لإدارة المجموعات المنفصلة
class UnionFind:
    # دالة البناء (Constructor) لتهيئة الهيكل
    def __init__(self, n):
        # مصفوفة الآباء: في البداية كل عنصر هو أب لنفسه (مجموعة مستقلة)
        self.parent = list(range(n))
        # مصفوفة الرتبة (Rank): تستخدم لتحسين عملية الدمج (تخزين ارتفاع الشجرة)
        self.rank = [0] * n

    # دالة البحث (Find) لمعرفة الجذر (المجموعة) التي ينتمي إليها العنصر i
    def find(self, i):
        # إذا لم يكن العنصر هو أب لنفسه (أي أنه تابع لعنصر آخر)
        if self.parent[i] != i:
            # (Path Compression): نجعل العنصر يشير مباشرة للجذر لتسريع البحث مستقبلاً
            self.parent[i] = self.find(self.parent[i])
        # إرجاع الجذر
        return self.parent[i]

    # دالة الدمج (Union) لربط مجموعتين ببعضهما
    def union(self, i, j):
        # نوجد جذر المجموعة الأولى
        root_i = self.find(i)
        # نوجد جذر المجموعة الثانية
        root_j = self.find(j)
        
        # إذا كان الجذران مختلفين (أي أنهما في مجموعتين منفصلتين)
        if root_i != root_j:
            # (Union by Rank): نربط الشجرة الأقصر تحت الشجرة الأطول لتقليل الارتفاع
            if self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            elif self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            else:
                # إذا تساوت الرتب، نربط أي واحدة بالأخرى ونزيد الرتبة
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            # نرجع True دليلاً على نجاح عملية الدمج
            return True
        # نرجع False إذا كانا في نفس المجموعة بالفعل (لا نحتاج لدمج)
        return False

# الدالة الرئيسية لتنفيذ الحل المحسن (Optimized MST)
def solve_optimized(num_buildings, all_edges):
    # ترتيب الكابلات تصاعدياً حسب الوزن (O(E log E))
    sorted_edges = sorted(all_edges, key=lambda x: x[2])
    
    # قائمة الحل النهائي
    mst_edges = []
    
    # التكلفة الكلية
    mst_cost = 0
    
    # إنشاء كائن Union-Find لعدد المباني الموجودة
    uf = UnionFind(num_buildings)
    
    # عداد الكابلات
    count = 0
    
    # المرور على الكابلات المرتبة
    for u, v, w in sorted_edges:
        # شرط التوقف
        if count == num_buildings - 1:
            break
            
        # --- الجزء المحسن (Optimized Part) ---
        # نحاول دمج النقطتين u و v.
        # دالة union ستقوم بالتأكد: هل هما في مجموعتين مختلفتين؟
        # إذا نعم: تدمجهما وترجع True (نقبل الكابل).
        # إذا لا (متصلين سابقاً): ترجع False (نرفض الكابل لتجنب الدائرة).
        # هذه العملية سريعة جداً (تقريباً O(1)).
        if uf.union(u, v):
            mst_edges.append((u, v, w))
            mst_cost += w
            count += 1
            
    # إرجاع النتيجة
    return mst_cost, mst_edges