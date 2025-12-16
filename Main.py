# main_analysis.py
import time         # لحساب الوقت
import random       # لتوليد الأرقام العشوائية
import math         # للعمليات الحسابية الجذرية

# استيراد الخوارزميتين من الملفات السابقة
from Algorithm_Naive import solve_naive
from Algorithm_Optimized import solve_optimized

# دالة مساعدة لحساب المسافة بين نقطتين (قانون إقليدس)
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# دالة لتوليد مباني عشوائية
def generate_data(num_buildings):
    buildings = []
    # حلقة تكرار لإنشاء إحداثيات (x, y) لكل مبنى
    for _ in range(num_buildings):
        x = random.randint(0, 1000)
        y = random.randint(0, 1000)
        buildings.append((x, y))
    
    # توليد كل الكابلات الممكنة بين المباني
    edges = []
    for i in range(num_buildings):
        for j in range(i + 1, num_buildings):
            # حساب المسافة واعتبارها "وزن" الكابل
            dist = calculate_distance(buildings[i], buildings[j])
            # تخزين الكابل كـ (نقطة1، نقطة2، الوزن)
            edges.append((i, j, dist))
            
    return edges

# نقطة انطلاق البرنامج
if __name__ == "__main__":
    print("--- Empirical Analysis Started ---")
    
    # قائمة بأحجام الاختبار المختلفة كما يطلب المشروع
    test_sizes = [10, 50, 100, 200, 300]
    
    # طباعة رأس الجدول
    print(f"{'Size':<10} | {'Naive Time':<15} | {'Optimized Time':<15}")
    print("-" * 50)
    
    for n in test_sizes:
        # 1. توليد البيانات لهذا الحجم
        edges = generate_data(n)
        
        # 2. قياس وقت الحل الساذج
        start1 = time.time()
        cost1, _ = solve_naive(n, edges) # استدعاء دالة algorithm1
        end1 = time.time()
        time1 = end1 - start1
        
        # 3. قياس وقت الحل المحسن
        start2 = time.time()
        cost2, _ = solve_optimized(n, edges) # استدعاء دالة algorithm2
        end2 = time.time()
        time2 = end2 - start2
        
        # طباعة النتائج في الجدول
        print(f"{n:<10} | {time1:.6f}s       | {time2:.6f}s")
        
        # التأكد من تطابق النتائج (للتأكد من صحة الحل)
        if int(cost1) != int(cost2):
            print("Error: Results do not match!")

    print("\n--- Done ---")